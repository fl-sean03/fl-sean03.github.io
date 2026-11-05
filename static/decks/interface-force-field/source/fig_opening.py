"""Figures for the opening. They show the peptide S7 on platinum, one amino acid changing the shape of a crystal,
separately built models against IFF, and the materials IFF covers."""
from functools import lru_cache

import numpy as np
from matplotlib.patches import Circle

import render as rt
import structures as st
from draw import (CRYSTAL_VIEWS, FLAT, WIDE, aim, arrow, ball_and_stick, canvas, dashed, front_view, layered,
                  magnifier, panel, platinum_scenes, polyhedral, pt, pt_crystal, save, shot, spheres, text)
from style import ACCENT, ACCENT_SOFT, BLUE, BODY, INK, LINE, MUTED, RULE, TEAL, TINT


@lru_cache
def polyethylene(carbons=20):
    """An all-trans polyethylene chain segment (a long alkane) with its backbone along x."""
    m = st.Molecule('C' * carbons, seed=3)
    for i in range(carbons - 3):
        m.twist(i, i + 1, i + 2, i + 3, 180.0)
    p = m.positions
    u = p[carbons - 1] - p[0]
    frame = np.array([u / np.linalg.norm(u), *np.linalg.svd(p[:carbons] - p[:carbons].mean(0))[2][1:]])
    return m, (p - p[:carbons].mean(0)) @ frame.T


@lru_cache
def tripeptide(sequence):
    """An extended strand with the backbone along x and the middle side chain pointing along +y."""
    m = st.Molecule(sequence=sequence, seed=11)
    p = m.extend()
    names = m.names
    backbone = [names[n, k] for n in (1, 2, 3) for k in ('N', 'CA', 'C')]
    centre = p[backbone].mean(0)
    u = np.linalg.svd(p[backbone] - centre)[2][0]
    if np.dot(p[names[3, 'C']] - p[names[1, 'N']], u) < 0:
        u = -u
    side = [i for i in m.residue(2) if i not in backbone and m.symbols[i] != 'H']

    def frame(p):
        v = p[side].mean(0) - p[names[2, 'CA']]
        v -= np.dot(v, u) * u
        v /= np.linalg.norm(v)
        return (p - centre) @ np.array([u, v, np.cross(u, v)]).T

    ring = [i for i in side if i in m.aromatic]
    if not ring:
        return m, frame(p), side
    best = None
    for chi2 in range(0, 180, 5):  # turn the flat ring to face the viewer
        m.twist(names[2, 'CA'], names[2, 'CB'], names[2, 'CG'], names[2, 'CD1'], chi2)
        q = frame(m.positions)
        normal = np.linalg.svd(q[ring] - q[ring].mean(0))[2][2]
        if best is None or abs(normal[2]) > best[0]:
            best = abs(normal[2]), q
    return m, best[1], side


def s7_on_platinum(name, ring=False):
    """S7 lying on Pt(111) in water, fading to white at the left, top and bottom behind the slide text, footer and page
    number; `ring` marks the phenylalanine ring's carbons."""
    fig, ax = canvas(1100, 1080)
    m, flat, _ = st.s7()
    pep = flat @ st.rotation((0, 0, 1), np.radians(-24)).T
    rotation = front_view(56)
    water = st.waters_around((-36, -32, 2.4), (36, 32, 7.0), pep, rotation, seed=4)
    solid, liquid = platinum_scenes(m, pep, st.metal_surface((24, 22, 3)), water, ring=ring)
    layered(ax, ((solid, {}), (liquid, {'contact': 0.5, 'fog': 0})), rotation, (0, 0, 1100, 1080), 37,
            centre=aim(rotation, pep.mean(0), (110, 40), 37), edges={'left': 440, 'top': 360, 'bottom': 200})
    return save(fig, name, quality=90)


def cover():
    """S7 lying on Pt(111) in water."""
    return s7_on_platinum('cover')


def hook():
    """TLT grows Pt cubes, TFT grows Pt tetrahedra: one amino acid changes the crystal shape (R13)."""
    fig, ax = canvas(*WIDE)
    rows = (('TLT', 'leucine', 'cube', 27.5, BLUE, 'Cubes', 'square'),
            ('TFT', 'phenylalanine', 'tetra', 44.0, TEAL, 'Tetrahedra', 'triangular'))
    for n, (seq, name, shape, size, color, shapes, pattern) in enumerate(rows):
        y0 = n * 364
        m, p, side = tripeptide(seq)
        scene = rt.Scene()
        ball_and_stick(scene, m.symbols, p, m.pairs)
        project = shot(ax, scene, FLAT, (0, y0, 560, 286), 24)
        ax.add_patch(Circle(project(p[side].mean(0)), 74, color=ACCENT_SOFT, zorder=1))
        for r, letter in enumerate(seq):
            x = project(p[[i for i in m.residue(r + 1) if m.symbols[i] != 'H']].mean(0))[0]
            text(ax, x, y0 + 300, letter, size=32, bold=True, color=ACCENT if r == 1 else INK, ha='center')
        text(ax, 280, y0 + 338, f'threonine · {name} · threonine', size=23, color=MUTED, ha='center')
        text(ax, 645, y0 + 128, 'grows', size=23, color=MUTED, ha='center')
        arrow(ax, (590, y0 + 160), (700, y0 + 160), color=LINE, width=4)
        shot(ax, pt_crystal(shape, size), CRYSTAL_VIEWS[shape], (720, y0, 340, 340), 7.0, centre=(0, 0, 0))
        magnifier(ax, (1172, y0 + 170), 84, '100' if shape == 'cube' else '111', color)
        text(ax, 1296, y0 + 118, shapes, size=36, bold=True, color=color)
        text(ax, 1296, y0 + 172, f'{pattern} pattern of', size=26, color=BODY)
        text(ax, 1296, y0 + 208, 'atoms on every face', size=26, color=BODY)
    return save(fig, 'hook')


def compat():
    """Separately built metal and molecule models against IFF's shared equation and combination rules (K21)."""
    fig, ax = canvas(*WIDE)
    metal_icon, molecule_icon = pt_crystal('cube', 3 * st.LATTICE['Pt']), rt.Scene()
    m, p, _ = tripeptide('TFT')
    ball_and_stick(molecule_icon, m.symbols, p, m.pairs)
    for side, (title, color, link, rule, value, claim) in enumerate((
            ('Built separately', MUTED, False, ['No shared rule for', 'metal with molecules'],
             'Up to 50% low', ['surface energies from metal-only', 'models (embedded-atom method)']),
            ('Interface Force Field', ACCENT, True, ['So metal–molecule pairs', 'follow the same rules'],
             'Within 5%', ['of measured surface and', 'water-interface energies']))):
        x0 = side * 894
        panel(ax, x0, 0, 834, 714, TINT)
        text(ax, x0 + 44, 58, title, size=32, bold=True, color=color)
        shot(ax, metal_icon, CRYSTAL_VIEWS['cube'], (x0 + 40, 100, 250, 220), 9.5, centre=(0, 0, 0))
        shot(ax, molecule_icon, FLAT, (x0 + 540, 100, 260, 220), 17)
        text(ax, x0 + 165, 350, 'Metal model', size=27, bold=True, ha='center')
        text(ax, x0 + 165, 388, 'its own equations' if not link else 'the molecules’ equations', size=24,
             color=BODY, ha='center')
        text(ax, x0 + 670, 350, 'Molecular model', size=27, bold=True, ha='center')
        text(ax, x0 + 670, 388, 'different equations' if not link else 'unchanged', size=24, color=BODY, ha='center')
        if link:
            ax.plot([x0 + 300, x0 + 530], [210, 210], color=ACCENT, lw=pt(5), zorder=3)
            ax.add_patch(Circle((x0 + 415, 210), 26, color=ACCENT, zorder=8))
            for dy in (-6.5, 6.5):  # an equals sign, the same rules, against the other panel's question mark
                ax.plot([x0 + 404, x0 + 426], [210 + dy, 210 + dy], color='white', lw=pt(5), zorder=9)
        else:
            dashed(ax, (x0 + 300, 210), (x0 + 380, 210), color=LINE, width=5)
            dashed(ax, (x0 + 450, 210), (x0 + 530, 210), color=LINE, width=5)
            ax.add_patch(Circle((x0 + 415, 210), 26, fc='white', ec=MUTED, lw=pt(3), zorder=8))
            text(ax, x0 + 415, 212, '?', size=30, bold=True, color=MUTED, ha='center', va='center_baseline', z=9)
        text(ax, x0 + 415, 458, rule[0], size=24, color=INK, ha='center')
        text(ax, x0 + 415, 490, rule[1], size=24, color=INK, ha='center')
        ax.plot([x0 + 44, x0 + 790], [548, 548], color=RULE, lw=pt(2), zorder=1)
        text(ax, x0 + 44, 612, value, size=44, bold=True, color=color)
        text(ax, x0 + 400, 596, claim[0], size=24, color=BODY)
        text(ax, x0 + 400, 630, claim[1], size=24, color=BODY)
    return save(fig, 'compat')


def catalog():
    """The solids IFF parameterizes, above the molecules it is combined with."""
    fig, ax = canvas(1728, 578)
    text(ax, 0, 12, 'SOLIDS AND THEIR SURFACES', size=18, bold=True, color=ACCENT)
    gold = st.nanocrystal('Au', 'cube', 5 * st.LATTICE['Au']).positions
    gold = gold[np.all(gold @ np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [-1, -1, -1], [-1, -1, 1],
                                        [-1, 1, -1], [1, -1, -1]]).T / np.sqrt(3) <= 11.0, axis=1)]
    scene = rt.Scene()
    spheres(scene, ['Au'] * len(gold), gold)
    shot(ax, scene, CRYSTAL_VIEWS['cube'], (0, 34, 400, 214), 6.8, centre=(0, 0, 0))
    scene = rt.Scene()
    polyhedral(scene, *st.silica((8, 8, 3), (2, 8, 2.5), (24, 22, 14)))
    shot(ax, scene, rt.view((0.3, -1, 0.45)), (442, 34, 400, 214), 11.5)
    scene = rt.Scene()
    polyhedral(scene, *st.block(st.hydroxyapatite(), (4, 4, 2), (0, 0, 0), (28, 22, 7.0)))
    shot(ax, scene, rt.view((0.15, -0.25, 1), (0, 1, 0)), (884, 34, 400, 214), 8.6)
    scene = rt.Scene()
    polyhedral(scene, *st.block(st.cod('1540704'), (3, 2, 3), (0, 0, 0), (30, 7.5, 21)))
    shot(ax, scene, rt.view((0.12, -1, 0.15)), (1326, 34, 400, 214), 8.4)
    for x, head, line in ((0, 'Metals', 'gold, platinum and other metals'),
                          (442, 'Silica', 'sand and glass, with OH groups'),
                          (884, 'Hydroxyapatite', 'the mineral in bone and teeth'),
                          (1326, 'Cement', 'tricalcium silicate')):
        text(ax, x + 200, 268, head, size=28, bold=True, ha='center')
        text(ax, x + 200, 302, line, size=23, color=MUTED, ha='center')
    text(ax, 0, 352, 'COMBINED WITH STANDARD MOLECULE MODELS SUCH AS AMBER, CHARMM, OPLS-AA AND PCFF', size=18,
         bold=True, color=TEAL)
    sym, pos = st.water_box((-11, -5, -4), (11, 5, 4), seed=2)
    drop = np.repeat(np.sum((pos[::3] / (11, 5, 4)) ** 2, axis=1) < 1, 3)  # a rounded droplet of liquid water
    scene = rt.Scene()
    ball_and_stick(scene, [e for e, k in zip(sym, drop) if k], pos[drop])
    shot(ax, scene, FLAT, (0, 380, 540, 140), 13)
    m, flat_pose, _ = st.s7()
    scene = rt.Scene()
    ball_and_stick(scene, m.symbols, flat_pose, m.pairs)
    shot(ax, scene, FLAT, (594, 380, 540, 140), 12)
    m, chain = polyethylene()
    scene = rt.Scene()
    ball_and_stick(scene, m.symbols, chain, m.pairs)
    shot(ax, scene, rt.view((0, -0.3, 1), (0, 1, 0)), (1188, 380, 540, 140), 20)
    for x, head in ((0, 'Water'), (594, 'Peptides and proteins'), (1188, 'Polymers')):
        text(ax, x + 270, 548, head, size=28, bold=True, ha='center')
    return save(fig, 'catalog')


FIGURES = (cover, hook, compat, catalog)
