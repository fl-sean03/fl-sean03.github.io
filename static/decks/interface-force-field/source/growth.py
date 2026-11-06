"""The rule behind the growth animation on slide 2. It illustrates an idea and is not a simulation from a paper.

Platinum atoms sit on the sites of an ideal face-centred cubic lattice, written as integer points (i, j, k) with
i + j + k even, in units of half the cubic cell (a/2 = 1.96 Å). The crystal starts as a cuboctahedron, SEED layers
from its centre to each of its six square {100} faces and to each of its eight triangular {111} faces. It grows one
atomic layer at a time on all 14 faces. Each new layer starts as an island around a random site of its face and
spreads in order of distance from that site, plus up to NOISE of random extra distance, until it covers the face.
Then the next layer starts. Each face starts at a random point in its first layer, so the faces do not keep step.

A square face adds one layer per unit of time and a triangular face, where the peptides lie, adds RATE of a layer.
With equal rates the cuboctahedron keeps its shape, because both kinds of face then move out in proportion to their
distance from the centre. With RATE = 1/4 the square faces shrink and vanish at t = 2 SEED, and the crystal is then
an octahedron, which has only triangular faces.

The peptide is TFT lying flat with its phenylalanine ring down, the pose of `structures.adsorbed`. One copy lies at
the centre of each triangular face from the start. More copies arrive, dropping DROP onto the face, wherever one
fits with its atoms at least MARGIN inside the face's edges and CLOSE from every other copy. A new layer starts away
from the peptides, and each copy steps up onto it just before its spreading edge arrives.
"""
import numpy as np

import structures as st

SEED, RATE, NOISE, MARGIN = 10, 0.25, 1.5, 1.0  # layers, layers per unit time, half cells, Å
UNIT = st.LATTICE['Pt'] / 2  # Å per lattice unit
HUNDRED = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
ONE11 = np.array([(x, y, z) for x in (1, -1) for y in (1, -1) for z in (1, -1)])
NORMALS = np.vstack([HUNDRED, ONE11])  # the 14 faces: plane index = normal · site, halved for {111}
DIRECTIONS = NORMALS / np.linalg.norm(NORMALS, axis=1)[:, None]
SPACING = np.where(np.arange(14) < 6, 1.0, 0.5)
RATES = np.where(np.arange(14) < 6, 1.0, RATE)
END = SEED / (1 - 2 * RATE)  # when the square faces vanish
LIFT, LAND, DROP = 0.75, 1.0, 10.0  # time a peptide takes to step up a layer and to land, and the Å it drops
CLOSE = 3.0  # Å within which a peptide atom touches a site or another copy's atom


class Growth:
    """The crystal and its peptides at any time from 0 to END, all fixed by `seed`."""

    def __init__(self, seed=3):
        rng = np.random.default_rng(seed)
        reach = int(END * RATE + SEED) * 2 + 2  # past the final octahedron's vertices
        grid = np.mgrid[-reach:reach + 1, -reach:reach + 1, -reach:reach + 1].reshape(3, -1).T
        grid = grid[(grid.sum(1) % 2 == 0) & (np.abs(grid).sum(1) <= reach)]
        self.sites = grid
        self.plane = (grid @ NORMALS.T * SPACING).astype(int)  # (sites, 14) plane index on every face
        self.phase = rng.uniform(0, 1, 14)
        index = {tuple(s): n for n, s in enumerate(grid)}
        bonds = [(i, j, k) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if abs(i) + abs(j) + abs(k) == 2]
        self.near = np.array([[index.get((x + i, y + j, z + k), -1) for i, j, k in bonds] for x, y, z in grid])
        self.bond_vectors = np.array(bonds, float)
        self.m = st.Molecule(sequence='TFT', conformers=24, seed=7)
        self.pose = st.adsorbed(self.m, 'flat')  # its ring 2.6 Å above a surface at z = 0
        self.peptides = self.place(rng)
        self.islands = {}
        for f in range(14):
            for layer in self.new_layers(f):
                self.islands[f, layer] = self.island(f, layer, rng)
        for p in self.peptides:
            p['lifts'] = self.lifts(p)

    # Time ------------------------------------------------------------------------------------------------------

    def started(self, f, layer):
        """When face f begins its layer `layer` (it completes 1 / RATES[f] later)."""
        return (layer - SEED - 1 - self.phase[f]) / RATES[f]

    def bounds(self, t):
        """Completed layers of every face at time t, as plane indices."""
        return SEED + np.floor(RATES * t + self.phase).astype(int)

    def new_layers(self, f):
        """The layers face f starts from t = 0 to END."""
        return range(SEED + 1, int(SEED + RATES[f] * END + self.phase[f]) + 2)

    # Islands ---------------------------------------------------------------------------------------------------

    def region(self, f, layer, t):
        """Sites of face f's layer `layer` inside every other face's completed layers at time t."""
        done = self.bounds(t)
        others = np.arange(14) != f
        return np.flatnonzero((self.plane[:, f] == layer) & np.all(self.plane[:, others] <= done[others], axis=1))

    def island(self, f, layer, rng):
        """The order in which a layer fills: noisy distance from a random nucleus clear of the peptides."""
        start, end = self.started(f, layer), self.started(f, layer + 1)
        sites = np.flatnonzero(self.plane[:, f] == layer)
        final = self.region(f, layer, end - 1e-9)
        if not len(final):
            return sites, np.full(len(sites), np.inf), 0.0
        clear = np.setdiff1d(self.region(f, layer, max(start, 0)), self.footprints(f, layer, max(start, 0)))
        nucleus = self.sites[rng.choice(clear if len(clear) else final)]
        dist = np.linalg.norm(self.sites[sites] - nucleus, axis=1) + rng.uniform(0, NOISE, len(sites))
        reach = dist[np.isin(sites, final)].max()
        return sites, dist, reach

    def spread(self, f, layer, t):
        """The island radius of face f's layer at time t (0 before it starts, its full reach once complete)."""
        reach = self.islands[f, layer][2]
        start, end = self.started(f, layer), self.started(f, layer + 1)
        return reach * np.sqrt(np.clip((t - start) / (end - start), 0, 1))

    def atoms(self, t):
        """Indices of the sites filled at time t."""
        done = self.bounds(t)
        over = self.plane - done
        inside = np.all(over <= 0, axis=1)
        edge = (np.sum(over == 1, axis=1) == 1) & np.all(over <= 1, axis=1)
        island = np.zeros(len(self.sites), bool)
        for f in range(14):
            key = (f, done[f] + 1)
            if key in self.islands:
                sites, dist, _ = self.islands[key]
                island[sites[dist <= self.spread(f, done[f] + 1, t)]] = True
        return np.flatnonzero(inside | (edge & island))

    def on_square(self, filled, t):
        """Which of the sites `filled` lie in the outer layer of a square face and of no triangular face."""
        top = self.plane[filled] >= self.bounds(t)
        return top[:, :6].any(1) & ~top[:, 6:].any(1)

    def surface(self, filled):
        """The filled sites with at least one empty neighbour, and each one's outward direction."""
        full = np.zeros(len(self.sites) + 1, bool)
        full[filled] = True
        empty = ~full[self.near[filled]]
        shown = empty.any(1)
        outward = empty[shown].astype(float) @ self.bond_vectors
        return filled[shown], outward / np.maximum(np.linalg.norm(outward, axis=1), 1e-9)[:, None]

    # Peptides --------------------------------------------------------------------------------------------------

    def frame(self, f):
        """Right-handed axes (in-plane x, in-plane y, outward normal) of face f."""
        n = DIRECTIONS[f]
        x = np.cross((0, 0, 1) if abs(n[2]) < 0.9 else (1, 0, 0), n)
        x /= np.linalg.norm(x)
        return np.array([x, np.cross(n, x), n])

    def height(self, f, layer):
        """Distance in Å from the centre to the plane of face f's layer `layer`."""
        return layer * UNIT / np.linalg.norm(NORMALS[f] * SPACING[f])

    def placed(self, p, layer, lift=0.0):
        """World positions of peptide p resting on face f's layer `layer`, raised `lift` Å more."""
        axes = self.frame(p['face'])
        c, s = np.cos(p['turn']), np.sin(p['turn'])
        local = self.pose @ np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]]).T + (*p['at'], lift)
        return local @ axes + (self.height(p['face'], layer) * axes[2])

    def clearance(self, f, p, t):
        """How far in Å peptide p, resting on face f at time t, stays inside the face's edges (negative if over)."""
        n, done = DIRECTIONS, self.bounds(t)
        heights = np.array([self.height(g, done[g]) for g in range(14)])
        points = self.placed(p, done[f])
        flat = points - np.outer(points @ n[f] - heights[f], n[f])  # dropped onto the face
        gaps = [np.min(heights[g] - flat @ n[g]) / np.linalg.norm(n[g] - (n[g] @ n[f]) * n[f])
                for g in range(14) if abs(n[g] @ n[f]) < 0.99]
        return min(gaps)

    def place(self, rng, tries=400):
        """Peptide copies on the eight triangular faces, each landing as soon as it fits MARGIN inside the edges. The
        first copy on each face sits at its centre from the start, turned to fit best, and the rest are tried at
        random."""
        times = np.linspace(0, END, 161)
        done = []
        for f in range(6, 14):
            turns = np.linspace(0, 2 * np.pi, 72, endpoint=False)
            best = max(turns, key=lambda a: self.clearance(f, dict(face=f, at=(0, 0), turn=a), 0))
            for n in range(tries):
                if n:
                    p = dict(face=f, at=rng.uniform(-60, 60, 2), turn=rng.uniform(0, 2 * np.pi))
                else:
                    p = dict(face=f, at=(0, 0), turn=best)
                points = self.placed(p, self.bounds(END)[f])
                if self.clearance(f, p, END) < MARGIN or any(
                        np.min(np.linalg.norm(points[:, None] - q['points'][None], axis=2)) < CLOSE for q in done):
                    continue
                p['points'] = points
                p['lands'] = 0.0 if not n else next(t for t in times if self.clearance(f, p, t) >= MARGIN)
                done.append(p)
        return done

    def distances(self, p, sites, layer):
        """How far in Å each of `sites` is from the nearest atom of peptide p resting on its face's layer `layer`."""
        points = self.placed(p, layer)
        return np.linalg.norm(self.sites[sites][:, None] * UNIT - points[None], axis=2).min(1)

    def footprints(self, f, layer, t):
        """Sites of face f's layer `layer` that would touch a peptide resting on the layer below at time t."""
        sites = np.flatnonzero(self.plane[:, f] == layer)
        under = [sites[self.distances(p, sites, layer - 1) < CLOSE] for p in self.peptides
                 if p['face'] == f and p['lands'] <= t]
        return np.concatenate([[], *under]).astype(int)

    def lifts(self, p):
        """When peptide p steps up onto each new layer of its face: just before that layer's island reaches it."""
        f, out = p['face'], []
        for layer in self.new_layers(f):
            sites, dist, reach = self.islands[f, layer]
            touch = self.distances(p, sites, layer - 1) < CLOSE
            if not touch.any() or reach == 0:
                continue
            first = dist[touch].min() - 0.5
            start, end = self.started(f, layer), self.started(f, layer + 1)
            out.append(start + (end - start) * np.clip(first / reach, 0, 1) ** 2)
        return out

    def peptide_at(self, p, t):
        """Peptide p's atoms at time t and how much of its landing is still to come (1 to 0), or None before then."""
        if p['lands'] and t < p['lands'] - LAND:
            return None
        ramps = np.clip((t - np.array(p['lifts']) + LIFT) / LIFT, 0, 1)
        steps = np.sum(ramps * ramps * (3 - 2 * ramps))  # each step up eases in and out
        coming = 1 - np.clip((t - p['lands'] + LAND) / LAND, 0, 1) if p['lands'] else 0.0
        return self.placed(p, SEED, steps * self.height(p['face'], 1) + DROP * coming ** 3), coming
