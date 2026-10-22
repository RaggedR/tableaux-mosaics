#!/usr/bin/env python3
"""
Mosaic representation and Purbhoo migration for KTW puzzles.

A mosaic is a tiling of a triangular grid by unit triangles and rhombi.
Each KTW puzzle defines a mosaic via its edge labeling (0, 1, 10).
Edges labeled 10 are shared edges of rhombus tiles.

The migration algorithm moves colored rhombi (the "flock") through
the mosaic via local hexagonal flips, producing the corresponding
LR tableau at the right boundary.

Coordinate conventions:
  - Level 0 = bottom (base of triangle, width N)
  - Level N = apex (width 0)
  - Vertex (r, j): level r, horizontal position j
  - Triangle side length N = n + m where n x m is the bounding box

Face types:
  - ('up', r, j) = upward triangle with vertices (r,j), (r,j+1), (r+1,j)
  - ('down', r, j) = downward triangle with vertices (r,j+1), (r+1,j), (r+1,j+1)

Edge types (by vertex pair):
  - Horizontal: ((r,j), (r,j+1))
  - NE slash /: ((r,j), (r+1,j))     [left edge of up_{r,j}]
  - NW backslash \\: ((r,j+1), (r+1,j))  [right edge of up_{r,j}]

Reference: Purbhoo, "Puzzles, Tableaux, and Mosaics" (arXiv:0705.1184)
"""

from collections import defaultdict
from copy import deepcopy

from lr_coefficients import (
    lr_puzzles, Puzzle, DELTA, NABLA,
    partition_to_boundary, boundary_to_partition, _bounding_box,
)


# ================================================================
# Edge geometry
# ================================================================

def edge_key(v1, v2):
    """Canonical edge key: lexicographically sorted vertex pair."""
    return (min(v1, v2), max(v1, v2))


def classify_edge(ek):
    """Classify edge as 'h' (horizontal), 'ne' (/ slash), or 'nw' (\\ backslash)."""
    (r1, j1), (r2, j2) = ek
    if r1 == r2:
        return 'h'
    elif j1 == j2:
        return 'ne'
    else:
        return 'nw'


# ================================================================
# Face geometry
# ================================================================

def up_edges(r, j):
    """Edge keys for triangle_{r,j} in DELTA order: (bottom, left/, right\\)."""
    return (
        edge_key((r, j), (r, j + 1)),      # bottom horizontal
        edge_key((r, j), (r + 1, j)),       # left / (NE)
        edge_key((r, j + 1), (r + 1, j)),   # right \\ (NW)
    )


def down_edges(r, j):
    """Edge keys for nabla_{r,j} in NABLA order: (top, right/, left\\).

    'top' is the horizontal edge at level r+1 (geometrically the upper edge).
    """
    return (
        edge_key((r + 1, j), (r + 1, j + 1)),  # top horizontal
        edge_key((r, j + 1), (r + 1, j + 1)),   # right / (NE)
        edge_key((r, j + 1), (r + 1, j)),        # left \\ (NW)
    )


def face_edges(face):
    """Edge keys for a face in tile-convention order."""
    kind, r, j = face
    if kind == 'up':
        return up_edges(r, j)
    else:
        return down_edges(r, j)


def face_vertices(face):
    """Vertices of a face."""
    kind, r, j = face
    if kind == 'up':
        return {(r, j), (r, j + 1), (r + 1, j)}
    else:
        return {(r, j + 1), (r + 1, j), (r + 1, j + 1)}


def all_faces(N):
    """Enumerate all faces in a triangular grid of side N."""
    faces = []
    for r in range(N):
        w = N - r
        for j in range(w):
            faces.append(('up', r, j))
        for j in range(w - 1):
            faces.append(('down', r, j))
    return faces


# ================================================================
# Mosaic
# ================================================================

class Mosaic:
    """A mosaic on a triangular grid of side N.

    Attributes:
        N:     triangle side length
        edges: dict mapping edge_key -> label in {0, 1, 10}
        lam, mu, nu: boundary partitions
        n, m:  bounding box dimensions
        _edge_to_faces: adjacency cache (edge -> list of faces)
    """

    def __init__(self, N, edges, lam, mu, nu, n, m):
        self.N = N
        self.edges = dict(edges)
        self.lam = lam
        self.mu = mu
        self.nu = nu
        self.n = n
        self.m = m
        self._edge_to_faces = None

    @classmethod
    def from_puzzle(cls, puzzle):
        """Create a Mosaic from a Puzzle object."""
        m = cls(
            N=puzzle.N,
            edges=puzzle.edge_labels(),
            lam=puzzle.lam,
            mu=puzzle.mu,
            nu=puzzle.nu,
            n=puzzle.n,
            m=puzzle.m,
        )
        return m

    def copy(self):
        """Deep copy of the mosaic."""
        m = Mosaic(self.N, self.edges, self.lam, self.mu, self.nu,
                   self.n, self.m)
        m._edge_to_faces = self._edge_to_faces  # share the cache (immutable)
        return m

    # ── Edge access ──────────────────────────────────────────────

    def get(self, v1, v2):
        """Get label of edge between v1 and v2."""
        return self.edges[edge_key(v1, v2)]

    def get_ek(self, ek):
        """Get label of edge by key."""
        return self.edges[ek]

    def set_ek(self, ek, label):
        """Set label of edge by key."""
        self.edges[ek] = label

    # ── Adjacency ────────────────────────────────────────────────

    def edge_to_faces(self):
        """Build and cache the edge -> faces adjacency map."""
        if self._edge_to_faces is None:
            etf = defaultdict(list)
            for face in all_faces(self.N):
                for ek in face_edges(face):
                    etf[ek].append(face)
            self._edge_to_faces = dict(etf)
        return self._edge_to_faces

    def adjacent_faces(self, ek):
        """Return the faces sharing edge ek (1 if boundary, 2 if internal)."""
        return self.edge_to_faces().get(ek, [])

    def neighbors_of_face(self, face):
        """Return faces adjacent to `face` (sharing an edge)."""
        nbrs = []
        for ek in face_edges(face):
            for f in self.adjacent_faces(ek):
                if f != face:
                    nbrs.append((f, ek))
        return nbrs

    # ── Face labels ──────────────────────────────────────────────

    def face_tile(self, face):
        """Return the tile triple for a face (in DELTA/NABLA convention)."""
        return tuple(self.edges[ek] for ek in face_edges(face))

    def is_valid_face(self, face):
        """Check if a face has a valid tile type."""
        kind = face[0]
        tile = self.face_tile(face)
        return tile in (DELTA if kind == 'up' else NABLA)

    def is_valid(self):
        """Check all faces have valid tile types."""
        return all(self.is_valid_face(f) for f in all_faces(self.N))

    # ── Rhombus detection ────────────────────────────────────────

    def rhombi(self):
        """Find all rhombus tiles. Returns list of edge keys with label 10."""
        return [ek for ek, label in self.edges.items() if label == 10]

    def rhombus_faces(self, ek):
        """Return the two faces forming the rhombus at edge ek (label 10)."""
        assert self.edges[ek] == 10, f"Edge {ek} is not a rhombus (label={self.edges[ek]})"
        return self.adjacent_faces(ek)

    def rhombus_orientation(self, ek):
        """Return the orientation of a rhombus: 'h', 'ne', or 'nw'."""
        return classify_edge(ek)

    # ── Hexagonal flip ───────────────────────────────────────────

    def find_flips(self, rhombus_ek):
        """Find all possible flips for a rhombus at edge `rhombus_ek`.

        A flip operates on 3 faces: the 2 faces of the rhombus plus one
        adjacent face. It replaces the current rhombus with a new one in
        a different orientation.

        Returns: list of (third_face, new_rhombus_ek, new_edge_labels)
        """
        assert self.edges[rhombus_ek] == 10
        rf = self.rhombus_faces(rhombus_ek)
        if len(rf) != 2:
            return []  # boundary rhombus, can't flip

        f1, f2 = rf
        flips = []

        # For each face of the rhombus, find neighbors that could be the third face.
        # The third face must share an edge with one rhombus face but NOT with the other.
        # More precisely: it shares an edge with one face, and the shared edge goes
        # through the same vertex as rhombus_ek.
        rhombus_verts = face_vertices(f1) & face_vertices(f2)  # the 2 vertices of ek

        for rf_face, other_face in [(f1, f2), (f2, f1)]:
            for nbr, shared_ek in self.neighbors_of_face(rf_face):
                if nbr == other_face:
                    continue  # skip the other rhombus face
                # Check that the shared edge goes through one of the rhombus vertices
                # (this ensures the 3 faces form a fan around a common vertex)
                nbr_verts = face_vertices(nbr)
                shared_verts = face_vertices(rf_face) & nbr_verts
                if not (shared_verts & rhombus_verts):
                    continue  # not adjacent at the rhombus vertex

                # We have a valid triple: (other_face, rf_face, nbr)
                # rf_face is the middle face, sharing edges with both
                flip = self._compute_flip(other_face, rf_face, nbr,
                                          rhombus_ek, shared_ek)
                if flip is not None:
                    flips.append((nbr, flip))

        return flips

    def _compute_flip(self, f_left, f_mid, f_right, ek_left, ek_right):
        """Compute the flipped edge labels for a triple of faces.

        f_left and f_mid share ek_left (currently 10).
        f_mid and f_right share ek_right.
        The flip should make ek_right = 10 and change ek_left.

        Returns: dict of {edge_key: new_label} for the 2 internal edges,
                 or None if no valid flip exists.
        """
        LABELS = (0, 1, 10)
        current = (self.edges[ek_left], self.edges[ek_right])

        for l1 in LABELS:
            for l2 in LABELS:
                if (l1, l2) == current:
                    continue
                if l2 != 10:
                    continue  # we want the flip to move the rhombus

                # Trial: ek_left=l1, ek_right=l2
                old_left = self.edges[ek_left]
                old_right = self.edges[ek_right]
                self.edges[ek_left] = l1
                self.edges[ek_right] = l2

                ok = (self.is_valid_face(f_left) and
                      self.is_valid_face(f_mid) and
                      self.is_valid_face(f_right))

                self.edges[ek_left] = old_left
                self.edges[ek_right] = old_right

                if ok:
                    return {ek_left: l1, ek_right: l2}

        return None

    def apply_flip(self, flip_labels):
        """Apply a flip (dict of edge_key -> new_label) to this mosaic."""
        for ek, label in flip_labels.items():
            self.edges[ek] = label

    def do_flip(self, rhombus_ek, third_face):
        """Flip a rhombus toward `third_face`. Returns new rhombus edge key."""
        for nbr, flip in self.find_flips(rhombus_ek):
            if nbr == third_face:
                self.apply_flip(flip)
                # Find the new rhombus edge key (the one set to 10)
                for ek, label in flip.items():
                    if label == 10:
                        return ek
        raise ValueError(f"No valid flip from {rhombus_ek} toward {third_face}")

    # ── Boundary analysis ────────────────────────────────────────

    def left_boundary_edges(self):
        """Left boundary (lambda) edges: the leftmost / edges at each band."""
        return [edge_key((r, 0), (r + 1, 0)) for r in range(self.N)]

    def right_boundary_edges(self):
        """Right boundary (mu) edges: the rightmost \\ edges at each band."""
        return [edge_key((r, self.N - r), (r + 1, self.N - r - 1))
                for r in range(self.N)]

    def bottom_boundary_edges(self):
        """Bottom boundary (nu) edges: horizontal edges at level 0."""
        return [edge_key((0, j), (0, j + 1)) for j in range(self.N)]

    def is_boundary_edge(self, ek):
        """Check if an edge is on the triangle boundary."""
        faces = self.adjacent_faces(ek)
        return len(faces) < 2

    # ── Display ──────────────────────────────────────────────────

    def levels(self):
        """Reconstruct puzzle-style levels from horizontal edge labels."""
        lvls = []
        for r in range(self.N + 1):
            w = self.N - r
            row = []
            for j in range(w):
                ek = edge_key((r, j), (r, j + 1))
                row.append(self.edges[ek])
            lvls.append(tuple(row))
        return lvls

    def __repr__(self):
        sym = {0: '0', 1: '1', 10: 'R'}
        lines = [f"Mosaic(N={self.N}, rhombi={len(self.rhombi())})"]
        for i, lv in enumerate(self.levels()):
            s = ' '.join(sym.get(x, '?') for x in lv)
            lines.append(f"  {'  ' * i}{s}")
        return '\n'.join(lines)

    def show_rhombi(self):
        """Print rhombus positions grouped by orientation."""
        h, ne, nw = [], [], []
        for ek in sorted(self.rhombi()):
            t = classify_edge(ek)
            if t == 'h':
                h.append(ek)
            elif t == 'ne':
                ne.append(ek)
            else:
                nw.append(ek)
        print(f"  Horizontal ({len(h)}): {h}")
        print(f"  Slash /    ({len(ne)}): {ne}")
        print(f"  Bslash \\   ({len(nw)}): {nw}")


# ================================================================
# Flip graph exploration
# ================================================================

def reachable_mosaics(mosaic, max_depth=20):
    """BFS over the flip graph from a starting mosaic.

    Returns dict: frozenset(edges.items()) -> (Mosaic, depth, path)
    """
    def state_key(m):
        return frozenset(m.edges.items())

    start = state_key(mosaic)
    visited = {start: (mosaic.copy(), 0, [])}
    frontier = [(mosaic.copy(), 0, [])]

    while frontier:
        m, depth, path = frontier.pop(0)
        if depth >= max_depth:
            continue

        for rk in m.rhombi():
            for third_face, flip in m.find_flips(rk):
                m2 = m.copy()
                m2.apply_flip(flip)
                sk = state_key(m2)
                if sk not in visited:
                    new_path = path + [(rk, third_face, flip)]
                    visited[sk] = (m2, depth + 1, new_path)
                    frontier.append((m2, depth + 1, new_path))

    return visited


# ================================================================
# Demo
# ================================================================

def demo():
    print("=" * 60)
    print("  Mosaic Representation & Flip Graph")
    print("=" * 60)

    lam, mu, nu = (2, 1), (2, 1), (3, 2, 1)
    puzzles = lr_puzzles(lam, mu, nu)
    print(f"\n  c^{nu}_{{{lam},{mu}}} = {len(puzzles)}")

    mosaics = [Mosaic.from_puzzle(p) for p in puzzles]

    for i, m in enumerate(mosaics):
        print(f"\n  --- Mosaic {i + 1} ---")
        print(m)
        m.show_rhombi()
        print(f"  Valid: {m.is_valid()}")

        # Count available flips
        total_flips = 0
        for rk in m.rhombi():
            flips = m.find_flips(rk)
            total_flips += len(flips)
        print(f"  Available flips: {total_flips}")

    # Check if puzzles are connected by flips
    print(f"\n  --- Flip Graph (BFS from Puzzle 1) ---")
    visited = reachable_mosaics(mosaics[0], max_depth=12)
    print(f"  Reachable mosaics: {len(visited)}")

    # Check if puzzle 2 is reachable
    sk2 = frozenset(mosaics[1].edges.items())
    if sk2 in visited:
        m2_found, depth, path = visited[sk2]
        print(f"  Puzzle 2 reachable at depth {depth}")
        print(f"  Path ({len(path)} flips):")
        for rk, third, flip in path:
            orient = classify_edge(rk)
            new_rk = [ek for ek, l in flip.items() if l == 10][0]
            new_orient = classify_edge(new_rk)
            print(f"    {rk} ({orient}) -> {new_rk} ({new_orient})")
    else:
        print("  Puzzle 2 NOT reachable!")

    # List all reachable mosaics and their rhombus counts
    print(f"\n  --- All reachable mosaics ---")
    by_depth = defaultdict(list)
    for sk, (m, depth, path) in visited.items():
        by_depth[depth].append(m)
    for d in sorted(by_depth):
        print(f"    Depth {d}: {len(by_depth[d])} mosaic(s)")

    print()


if __name__ == '__main__':
    demo()
