"""Atomic structures for the pictures, built from open crystal data and standard geometry.

Crystals come from Crystallography Open Database files in data/structures (public domain) or from
published lattice constants. Molecules are RDKit conformers. Arrangements of molecules on surfaces
are illustrative constructions, not simulation snapshots.
"""
import itertools
import warnings
from functools import cached_property, lru_cache

import numpy as np
from ase import Atoms
from ase.build import fcc100, fcc111
from ase.data import covalent_radii, atomic_numbers
from ase.io import read
from scipy.optimize import minimize
from scipy.spatial import cKDTree

from style import DATA

LATTICE = {'Pt': 3.9231, 'Au': 4.07825, 'Rh': 3.8032}  # COD 9008480, COD 9008463, K21 Table 2
FCC = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])  # a face-centred cubic cell's 4 atoms
WATER_OH, WATER_ANGLE = 0.9572, 104.52  # standard water geometry (also the TIP3P geometry)
ION_RADII = {'Na': 1.02, 'Cl': 1.81}  # Å, Shannon ionic radii; together 2.83 Å, the Na-Cl spacing in salt
SI_O, O_SI_O, SI_O_SI = 1.60, 109.47, 146.7  # cristobalite's mean Si–O bond (Å) and angles (°), COD 9009686
STIFFNESS = (1000, 100, 3)  # relative springs on a Si–O bond (per Å²), an O–Si–O and a Si–O–Si angle (per rad²)


def cod(code):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return read(DATA / 'structures' / f'{code}.cif')


def rotation_between(a, b):
    """Rotation matrix turning direction a onto direction b."""
    a, b = np.asarray(a, float) / np.linalg.norm(a), np.asarray(b, float) / np.linalg.norm(b)
    v, c = np.cross(a, b), np.dot(a, b)
    if np.isclose(c, -1):
        axis = np.cross(a, [1, 0, 0] if abs(a[0]) < 0.9 else [0, 1, 0])
        return rotation(axis, np.pi)
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + vx + vx @ vx / (1 + c)


def rotation(axis, angle):
    axis = np.asarray(axis, float) / np.linalg.norm(axis)
    x, y, z = axis
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c + x * x * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                     [y * x * (1 - c) + z * s, c + y * y * (1 - c), y * z * (1 - c) - x * s],
                     [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z * z * (1 - c)]])


def bonds(symbols, positions, extra=0.18):
    """Pairs closer than the sum of covalent radii plus a small tolerance."""
    positions = np.asarray(positions, float)
    radii = np.array([covalent_radii[atomic_numbers[s]] for s in symbols])
    pairs = cKDTree(positions).query_pairs(2 * radii.max() + extra)
    return sorted((i, j) for i, j in pairs
                  if np.linalg.norm(positions[i] - positions[j]) < radii[i] + radii[j] + extra)


def water(rng=None):
    """One water molecule centred on its oxygen, randomly oriented when rng is given."""
    half = np.radians(WATER_ANGLE / 2)
    pos = np.array([[0, 0, 0], [np.sin(half), 0, np.cos(half)], [-np.sin(half), 0, np.cos(half)]])
    pos[1:] *= WATER_OH
    if rng is not None:
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        w, x, y, z = q
        R = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                      [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                      [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
        pos = pos @ R.T
    return ['O', 'H', 'H'], pos


def water_box(lo, hi, avoid=(), seed=1, density=0.0334, gap=2.75, clearance=2.6):
    """Liquid-density water (molecules per Å³) placed at random with an O–O gap; avoids given atoms."""
    rng = np.random.default_rng(seed)
    lo, hi = np.asarray(lo, float), np.asarray(hi, float)
    target = int(density * np.prod(hi - lo))
    avoid = np.asarray(avoid, float).reshape(-1, 3)
    blocked = cKDTree(avoid) if len(avoid) else None
    oxygens, symbols, positions = [], [], []
    for _ in range(target * 60):
        if len(oxygens) >= target:
            break
        o = lo + rng.random(3) * (hi - lo)
        if oxygens and np.min(np.linalg.norm(np.array(oxygens) - o, axis=1)) < gap:
            continue
        if blocked is not None and blocked.query(o)[0] < clearance:
            continue
        oxygens.append(o)
        sym, pos = water(rng)
        symbols += sym
        positions += list(pos + o)
    return symbols, np.array(positions).reshape(-1, 3)


def waters_around(lo, hi, molecule, rotation, seed, margin=1.2):
    """Liquid water in a box around a molecule, leaving out any water molecule that would overlap it on screen
    (in front or behind) for a camera with this rotation."""
    symbols, positions = water_box(lo, hi, avoid=molecule, seed=seed)
    tree = cKDTree((np.asarray(molecule) @ rotation.T)[:, :2])
    near = tree.query((positions @ rotation.T)[:, :2])[0] < 1.0 + margin
    keep = np.repeat(~near.reshape(-1, 3).any(1), 3)
    return [s for s, k in zip(symbols, keep) if k], positions[keep]


class Molecule:
    """An RDKit molecule with hydrogens and MMFF-relaxed conformers."""

    def __init__(self, smiles=None, sequence=None, conformers=1, seed=7):
        from rdkit import Chem
        from rdkit.Chem import AllChem
        mol = Chem.MolFromSequence(sequence) if sequence else Chem.MolFromSmiles(smiles)
        self.mol = Chem.AddHs(mol, addResidueInfo=bool(sequence))
        params = AllChem.ETKDGv3()
        params.randomSeed = seed
        ids = list(AllChem.EmbedMultipleConfs(self.mol, conformers, params))
        if not ids:
            raise ValueError(f'No conformer for {smiles or sequence}')
        AllChem.MMFFOptimizeMoleculeConfs(self.mol, maxIters=2000)
        self.symbols = [a.GetSymbol() for a in self.mol.GetAtoms()]
        self.pairs = [(b.GetBeginAtomIdx(), b.GetEndAtomIdx()) for b in self.mol.GetBonds()]
        self.conformers = [self.mol.GetConformer(i).GetPositions() for i in ids]

    @property
    def positions(self):
        """The first conformer's positions, as `twist` and `extend` leave them."""
        return self.mol.GetConformer(0).GetPositions()

    @cached_property
    def names(self):
        """Atom index by (residue number, PDB atom name), for a peptide."""
        return {(a.GetPDBResidueInfo().GetResidueNumber(), a.GetPDBResidueInfo().GetName().strip()): a.GetIdx()
                for a in self.mol.GetAtoms()}

    @cached_property
    def aromatic(self):
        """Indices of the aromatic atoms."""
        return {a.GetIdx() for a in self.mol.GetAtoms() if a.GetIsAromatic()}

    def residue(self, number):
        """Atom indices of one residue of a peptide (1-based, side chain and backbone)."""
        return [a.GetIdx() for a in self.mol.GetAtoms() if a.GetPDBResidueInfo().GetResidueNumber() == number]

    def hydrogens(self, i):
        """Indices of the hydrogen atoms bonded to atom i."""
        return [a.GetIdx() for a in self.mol.GetAtomWithIdx(i).GetNeighbors() if a.GetSymbol() == 'H']

    def ring(self):
        """Atom indices of the first aromatic six-membered ring."""
        for ring in self.mol.GetRingInfo().AtomRings():
            if len(ring) == 6 and all(self.mol.GetAtomWithIdx(i).GetIsAromatic() for i in ring):
                return list(ring)
        raise ValueError('No aromatic ring')

    def twist(self, a, b, c, d, degrees):
        """Set the first conformer's dihedral angle a-b-c-d, moving the atoms on the d side."""
        from rdkit.Chem import rdMolTransforms
        rdMolTransforms.SetDihedralDeg(self.mol.GetConformer(0), a, b, c, d, degrees)

    def extend(self, phi=-135.0, psi=135.0):
        """Set every backbone torsion of a peptide to a straight strand; returns the positions."""
        names = self.names
        count = max(n for n, _ in names)
        for n in range(1, count + 1):
            N, CA, C = names[n, 'N'], names[n, 'CA'], names[n, 'C']
            if n > 1:
                self.twist(names[n - 1, 'C'], N, CA, C, phi)
            if n < count:
                self.twist(N, CA, C, names[n + 1, 'N'], psi)
        return self.positions


def _flat_frame(pos, ring):
    """Rotation putting the ring in the xy plane with the rest of the molecule above it."""
    centre = pos[ring].mean(0)
    normal = np.linalg.svd(pos[ring] - centre)[2][2]
    rest = np.setdiff1d(np.arange(len(pos)), ring)
    if np.dot(pos[rest].mean(0) - centre, normal) < 0:
        normal = -normal
    return rotation_between(normal, (0, 0, 1)), centre


def _upright_frame(pos, ring, anchor):
    """Rotation standing the ring on edge with its attachment atom straight above it."""
    centre = pos[ring].mean(0)
    normal = np.linalg.svd(pos[ring] - centre)[2][2]
    up = pos[anchor] - centre
    up = up - np.dot(up, normal) * normal
    up /= np.linalg.norm(up)
    return np.array([normal, np.cross(up, normal), up]), centre


def adsorbed(molecule, pose='flat', height=2.6):
    """Positions of the molecule lying on a surface at z = 0 with its ring flat or standing upright.

    The conformer that best fits the pose is relaxed with MMFF while every heavy atom is held in a
    height window: the ring `height` Å up, and the rest low (flat) or lifted clear (upright). The long
    axis then runs along x. An illustrative pose, not an adsorption calculation.
    """
    ring = molecule.ring()
    anchor = next(n.GetIdx() for i in ring for n in molecule.mol.GetAtomWithIdx(i).GetNeighbors()
                  if n.GetIdx() not in ring and n.GetSymbol() == 'C')
    rest = np.setdiff1d(np.arange(len(molecule.symbols)), ring)
    flat = pose == 'flat'
    best = None
    for pos in molecule.conformers:
        frame, centre = _flat_frame(pos, ring) if flat else _upright_frame(pos, ring, anchor)
        p = (pos - centre) @ frame.T
        floor = 0.0 if flat else p[ring, 2].min()
        below = np.clip(floor + 0.3 - p[rest, 2], 0, None).sum()
        score = 6 * below + np.percentile(p[:, 2] - floor, 90) * (1 if flat else 0.25)
        if best is None or score < best[0]:
            best = (score, p - (0, 0, floor - height))
    hydrogen = np.array([s == 'H' for s in molecule.symbols])
    low = np.where(hydrogen, height - 0.7, height + (0.2 if flat else 0.8))
    high = np.where(hydrogen, np.inf, height + (3.6 if flat else 9.0))
    low[ring], high[ring] = height - 0.05, height + (0.05 if flat else 3.2)
    p = settle(molecule, best[1], low, high)
    xy = p[:, :2] - p[ring, :2].mean(0)
    angle = np.arctan2(*np.linalg.svd(xy - xy.mean(0))[2][0][::-1])
    p = p @ rotation((0, 0, 1), -angle).T
    p[:, :2] -= p[ring, :2].mean(0)
    return p


@lru_cache
def s7():
    """The Pt{111}-binding peptide S7, SSFPQPN (R13), and its two illustrative poses on a metal at z = 0."""
    m = Molecule(sequence='SSFPQPN', conformers=24, seed=7)
    return m, adsorbed(m, 'flat'), adsorbed(m, 'upright')


def settle(molecule, positions, low, high, rounds=12, step=0.6, far=25.0, slack=1.5, k=40.0):
    """MMFF relaxation moving each atom's height into [low, high], at most `step` Å per round.

    RDKit has no plane restraint, so height is a distance window to a fixed point `far` Å below the
    atom. Distance windows alone let the molecule swing around those points, so two more fixed points
    `far` Å away along x and y keep each round's sideways motion within `slack` Å.
    """
    from rdkit.Chem import AllChem
    from rdkit.Geometry import Point3D
    conf = molecule.mol.GetConformer(0)
    props = AllChem.MMFFGetMoleculeProperties(molecule.mol)
    pos = np.asarray(positions, float)
    for _ in range(rounds):
        lo, hi = np.minimum(low, pos[:, 2] + step), np.maximum(high, pos[:, 2] - step)
        hi = np.minimum(hi, 1e3)
        for i, p in enumerate(pos):
            conf.SetAtomPosition(i, Point3D(*p))
        ff = AllChem.MMFFGetMoleculeForceField(molecule.mol, props, confId=0)
        points = [[ff.AddExtraPoint(x, y, -far, fixed=True) - 1, ff.AddExtraPoint(x + far, y, z, fixed=True) - 1,
                   ff.AddExtraPoint(x, y + far, z, fixed=True) - 1] for x, y, z in pos.tolist()]
        ff.Initialize()
        for i, (below, side_x, side_y) in enumerate(points):
            ff.MMFFAddDistanceConstraint(i, below, False, far + lo[i], far + hi[i], k)
            ff.MMFFAddDistanceConstraint(i, side_x, False, far - slack, far + slack, k)
            ff.MMFFAddDistanceConstraint(i, side_y, False, far - slack, far + slack, k)
        ff.Minimize(maxIts=600)
        pos = conf.GetPositions()
    return pos


def block(bulk, repeat, lo, hi, centres=('Si', 'P'), cutoff=1.8):
    """Atoms of a repeated crystal inside a box, keeping every SiO4/PO4 group whole and hydroxide H with its O. A
    slab repeats only along its periodic directions."""
    big = bulk.repeat(tuple(n + 2 if along else 1 for n, along in zip(repeat, bulk.pbc)))
    symbols = np.array(big.get_chemical_symbols())
    pos = big.positions - bulk.cell.array[bulk.pbc].sum(axis=0)  # a spare cell on every side keeps groups whole
    inside = np.all((pos >= lo) & (pos <= hi), axis=1)
    tree = cKDTree(pos)
    centre = np.isin(symbols, centres)
    keep = inside & ~np.isin(symbols, ('O', 'H'))
    for i in np.flatnonzero(centre & inside):
        keep[[j for j in tree.query_ball_point(pos[i], cutoff) if symbols[j] == 'O']] = True
    bonded = np.array([any(centre[j] for j in tree.query_ball_point(p, cutoff)) for p in pos])
    keep |= inside & (symbols == 'O') & ~bonded  # free oxide and hydroxide oxygen
    for i in np.flatnonzero(symbols == 'H'):
        o = [j for j in tree.query_ball_point(pos[i], 1.1) if symbols[j] == 'O']
        keep[i] = bool(o) and keep[o[0]]
    return list(symbols[keep]), pos[keep]


def fcc_slab(element, face, size):
    """An fcc (111) or (100) slab, `size` = (atoms along x, atoms along y, layers), in an orthogonal cell."""
    build = fcc111 if face == '111' else fcc100
    return build(element, size=size, a=LATTICE[element], orthogonal=True)


def metal_surface(size, element='Pt', face='111'):
    """The (symbols, positions) of an fcc slab (see `fcc_slab`) with its top layer at z = 0, centred in x and y."""
    slab = fcc_slab(element, face, size)
    p = slab.positions
    return slab.get_chemical_symbols(), p - [*p[:, :2].mean(0), p[:, 2].max()]


def nanocrystal(element, shape, size):
    """Atoms of an ideal fcc crystal inside a cube ({100} faces) or tetrahedron ({111} faces)."""
    a = LATTICE[element]
    n = int(np.ceil(size / a)) + 2
    cells = np.array(list(itertools.product(range(-n, n + 1), repeat=3)), float)
    pos = ((cells[:, None, :] + FCC[None]) * a).reshape(-1, 3)
    if shape == 'cube':
        keep = np.all(np.abs(pos) <= size / 2 + 1e-6, axis=1)
    else:
        normals = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3)
        keep = np.all(pos @ normals.T <= size / (2 * np.sqrt(6)) + 1e-6, axis=1)  # inradius of edge `size`
    pos = pos[keep]
    pos -= pos.mean(0)
    return Atoms(element * len(pos), positions=pos)


def hydroxyapatite():
    """Ca10(PO4)6(OH)2 from COD 9011091 with every hydroxide column in one ordered orientation."""
    hap = cod('9011091')
    frac = hap.get_scaled_positions()
    symbols = np.array(hap.get_chemical_symbols())
    on_axis = np.linalg.norm(frac[:, :2] - np.round(frac[:, :2]), axis=1) < 1e-3
    phase = frac[:, 2] % 0.5
    drop = on_axis & (((symbols == 'O') & ~np.isclose(phase, 0.195, atol=0.01))
                      | ((symbols == 'H') & ~np.isclose(phase, 0.0608, atol=0.01)))
    del hap[np.flatnonzero(drop)]
    assert sorted(hap.get_chemical_formula('hill')) == sorted('Ca10H2O26P6'), hap.get_chemical_formula()
    return hap


def cap(symbols, positions, broken, top, length=0.96):
    """Add hydrogen to each broken O above height `top`, pointing away from its centre and upward."""
    symbols, positions = list(symbols), np.asarray(positions, float)
    centres = [i for i, s in enumerate(symbols) if s in ('Si', 'P')]
    tree = cKDTree(positions[centres])
    extra = []
    for i in np.flatnonzero(broken):
        if positions[i, 2] < top:
            continue
        j = centres[tree.query(positions[i])[1]]
        away = positions[i] - positions[j]
        direction = away / np.linalg.norm(away) + np.array([0, 0, 1.2])
        extra.append(positions[i] + length * direction / np.linalg.norm(direction))
    return symbols + ['H'] * len(extra), np.vstack([positions, *extra]) if extra else positions


@lru_cache
def silica(repeat, lo, hi):
    """A quartz block (COD 9000775) whose top face carries silanol groups: H on each O that lost its second Si.
    Returns (symbols, positions) with the top atom at z = 0, centred in x and y."""
    symbols, positions = block(cod('9000775'), repeat, lo, hi, centres=('Si',))
    symbols = np.array(symbols)
    si = cKDTree(positions[symbols == 'Si'])
    broken = (symbols == 'O') & np.array([len(si.query_ball_point(q, 1.8)) == 1 for q in positions])
    symbols, positions = cap(list(symbols), positions, broken, top=positions[:, 2].max() - 1.2)
    return symbols, positions - [*positions[:, :2].mean(0), positions[:, 2].max()]


def minimum_image(d, cell):
    """Differences `d` between atoms of a slab periodic along x and y with lengths `cell`, each to the nearest copy."""
    d = np.array(d, float)
    d[..., :2] -= cell * np.round(d[..., :2] / cell)
    return d


def angles(bonds, count):
    """Every (i, j, k) with bonds i–j and j–k, among `count` atoms."""
    around = [[] for _ in range(count)]
    for i, j in bonds:
        around[i].append(j)
        around[j].append(i)
    return np.array([(i, j, k) for j, ends in enumerate(around) for n, i in enumerate(ends) for k in ends[n + 1:]])


def relax(symbols, positions, bonds, free, cell):
    """Move the atoms `free` of a periodic slab to minimise a spring energy. Each Si–O bond pulls toward SI_O and
    each O–Si–O and Si–O–Si angle toward O_SI_O and SI_O_SI, with the relative stiffnesses in STIFFNESS."""
    b, a = np.array(bonds), angles(bonds, len(symbols))
    silicon = np.asarray(symbols)[a[:, 1]] == 'Si'
    ideal = np.radians(np.where(silicon, O_SI_O, SI_O_SI))
    kb, ka = STIFFNESS[0], np.where(silicon, *STIFFNESS[1:])
    x = np.array(positions, float)

    def energy(flat):
        x[free] = flat.reshape(-1, 3)
        grad = np.zeros_like(x)
        d = minimum_image(x[b[:, 1]] - x[b[:, 0]], cell)
        r = np.linalg.norm(d, axis=1)
        f = (2 * kb * (r - SI_O) / r)[:, None] * d
        np.add.at(grad, b[:, 1], f)
        np.add.at(grad, b[:, 0], -f)
        u, v = minimum_image(x[a[:, 0]] - x[a[:, 1]], cell), minimum_image(x[a[:, 2]] - x[a[:, 1]], cell)
        lu, lv = np.linalg.norm(u, axis=1)[:, None], np.linalg.norm(v, axis=1)[:, None]
        cos = np.clip((u * v).sum(1, keepdims=True) / (lu * lv), -0.999999, 0.999999)
        theta = np.arccos(cos[:, 0])
        g = (-2 * ka * (theta - ideal) / np.sqrt(1 - cos[:, 0] ** 2))[:, None]
        gu, gv = g * (v / (lu * lv) - cos * u / lu ** 2), g * (u / (lu * lv) - cos * v / lv ** 2)
        np.add.at(grad, a[:, 0], gu)
        np.add.at(grad, a[:, 2], gv)
        np.add.at(grad, a[:, 1], -gu - gv)
        return kb * ((r - SI_O) ** 2).sum() + (ka * (theta - ideal) ** 2).sum(), grad[free].ravel()

    best = minimize(energy, x[free].ravel(), jac=True, method='L-BFGS-B', options={'maxiter': 5000})
    x[free] = best.x.reshape(-1, 3)
    return x


@lru_cache
def cristobalite_surface(heated=False, cells=(2, 4), depth=12.0):
    """A slab of α-cristobalite (COD 9009686) with its (101) face up, periodic along x and y, top Si layer at z = 0.

    The cut runs through the widest gap between Si layers, so each Si on either face loses one bond, and an H on
    each O left with one Si makes a silanol, ≡Si–OH. The top face is then the Q3 surface, 4.7 OH per nm² (E14).
    Heated, each top silanol condenses with its nearest neighbour, 2 ≡Si–OH → ≡Si–O–Si≡ + H₂O, so every top Si
    has four bridging O. That is the Q4 surface, with no OH (E14). Each new bridge closes a strained ring of three
    Si, and `relax` moves every atom more than 3 Å above the bottom. Returns the slab and its new bridge O."""
    bulk = cod('9009686')
    a, _, c = bulk.cell.lengths()
    x, y = np.array([a, 0, -c]), np.array([0, a, 0])  # [10-1] and [010] lie in the (101) face
    frame = np.array([x / np.linalg.norm(x), y / a, np.cross(x, y) / np.linalg.norm(np.cross(x, y))])
    cell = np.array([cells[0] * np.linalg.norm(x), cells[1] * a])
    big = bulk.repeat(8)
    symbols = np.array(big.get_chemical_symbols())
    pos = (big.positions - big.positions.mean(0)) @ frame.T
    heights = np.sort(pos[symbols == 'Si', 2])
    heights = heights[np.abs(heights) < 4]
    gap = np.argmax(np.diff(heights))
    top = (heights[gap] + heights[gap + 1]) / 2
    inside = np.all(np.abs(pos[:, :2]) < cell / 2, axis=1) & (pos[:, 2] < top) & (pos[:, 2] > top - depth)
    si = pos[inside & (symbols == 'Si')]
    o = pos[symbols == 'O']
    o = o[cKDTree(si).query(o)[0] < 1.8]  # O bonded to a kept Si, then one copy of each under the period
    o[:, :2] = (o[:, :2] + cell / 2) % cell - cell / 2
    o = o[np.unique(np.round(o, 3), axis=0, return_index=True)[1]]
    symbols, positions = ['Si'] * len(si) + ['O'] * len(o), np.vstack([si, o])
    bonds = sorted(cKDTree(np.c_[positions[:, :2] % cell, positions[:, 2]], boxsize=[*cell, 0]).query_pairs(1.8))
    owner = {}
    for i, j in bonds:
        owner.setdefault(j, []).append(i)
    silanols = [j for j, s in owner.items() if len(s) == 1]
    for j in silanols:  # an H 0.96 Å out, with Si–O–H at 118° and the H tilted away from the slab
        away = minimum_image(positions[j] - positions[owner[j][0]], cell)
        away /= np.linalg.norm(away)
        out = np.array([0, 0, np.sign(away[2])]) - away[2] * np.sign(away[2]) * away
        h = np.cos(np.radians(62)) * away + np.sin(np.radians(62)) * out / np.linalg.norm(out)
        bonds.append((j, len(symbols)))
        symbols.append('H')
        positions = np.vstack([positions, positions[j] + 0.96 * h])
    bridges = []
    if heated:
        tops = {owner[j][0]: j for j in silanols if positions[j, 2] > top - 3}  # each top Si and its OH
        t = np.array(sorted(tops))
        gaps = np.linalg.norm(minimum_image(positions[t][:, None] - positions[t][None], cell), axis=2)
        partner = (gaps + 1e9 * np.eye(len(t))).argmin(1)
        assert np.all(partner[partner] == np.arange(len(t))), 'nearest top neighbours are not mutual'
        pairs = [(t[m], t[n]) for m, n in enumerate(partner) if m < n]
        hydrogen = {j: k for j, k in bonds if symbols[k] == 'H'}
        gone = set()
        for keep, give in pairs:  # Si `give` bonds to the O of Si `keep`, and its own O leaves with both H
            gone |= {tops[give], hydrogen[tops[keep]], hydrogen[tops[give]]}
            bonds.append((give, tops[keep]))
        kept = [k for k in range(len(symbols)) if k not in gone]
        index = {k: m for m, k in enumerate(kept)}
        symbols, positions = [symbols[k] for k in kept], positions[kept]
        bonds = sorted(tuple(sorted((index[i], index[j]))) for i, j in bonds if i in index and j in index)
        bridges = [index[tops[keep]] for keep, _ in pairs]
        free = np.flatnonzero(positions[:, 2] > positions[:, 2].min() + 3)
        positions = relax(symbols, positions, [(i, j) for i, j in bonds if 'H' not in (symbols[i], symbols[j])],
                          free, cell)
    slab = Atoms(symbols, positions - (0, 0, heights[gap]), cell=[*cell, 0], pbc=(True, True, False))
    return slab, tuple(bridges)


def silica_surface(heated, size, turn=0.0):
    """The slab of `cristobalite_surface` turned `turn` degrees about z and repeated over `size` (x, y) Å with every
    SiO4 group whole, centred on x = y = 0. Returns symbols, positions and a mask of the O that heating made into
    bridges."""
    slab, bridges = cristobalite_surface(heated)
    cell = slab.cell.lengths()[:2]
    spin = rotation((0, 0, 1), np.radians(turn))
    turned = Atoms(slab.symbols, slab.positions @ spin.T, cell=slab.cell.array @ spin.T, pbc=slab.pbc)
    repeat = np.ceil((np.linalg.norm(size) + 4) / cell).astype(int) - 2  # wide enough at any turn
    middle = (repeat - 1) / 2 @ turned.cell.array[:2]
    half = np.array([*np.divide(size, 2), np.inf])
    symbols, positions = block(turned, (*repeat, 1), middle - half, middle + half, centres=('Si',))
    gaps = minimum_image(positions[:, None] @ spin - slab.positions[list(bridges)][None], cell)
    return symbols, positions - middle, (np.linalg.norm(gaps, axis=2) < 1e-3).any(1)
