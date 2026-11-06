"""Figures for the opening. They show the peptide S7 on platinum, one amino acid changing the shape of a crystal,
an animation of the idea behind it, separately built models against IFF, and the materials IFF covers."""
from functools import lru_cache

import numpy as np
from matplotlib.patches import Circle
from PIL import Image

import growth as gr
import render as rt
import structures as st
from draw import (CRYSTAL_VIEWS, FLAT, aim, animate, arrow, ball_and_stick, canvas, dashed, front_view, layered,
                  magnifier, mix, panel, platinum_scenes, polyhedral, pt, pt_crystal, save, shot, spheres, text)
from style import (ACCENT, ACCENT_SOFT, ANIMATION, ASSETS, BLUE, BODY, ELEMENTS, GUTTER, INK, LINE, MUTED, RULE,
                   TEAL, TINT)


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
    """With TLT platinum grows as cubes, and with TFT it shifts toward tetrahedra, so one amino acid changes the crystal
    shape (R13). It leaves the right of its row to the growth animation."""
    fig, ax = canvas(1728 - ANIMATION - GUTTER)
    rows = (('TLT', 'leucine', 'grows', 'cube', 27.5, BLUE, 'Cubes', 'square'),
            ('TFT', 'phenylalanine', 'shifts toward', 'tetra', 44.0, TEAL, 'Tetrahedra', 'triangular'))
    for n, (seq, name, verb, shape, size, color, shapes, pattern) in enumerate(rows):
        y0 = n * 334
        m, p, side = tripeptide(seq)
        scene = rt.Scene()
        ball_and_stick(scene, m.symbols, p, m.pairs)
        project = shot(ax, scene, FLAT, (0, y0, 380, 252), 22)
        ax.add_patch(Circle(project(p[side].mean(0)), 68, color=ACCENT_SOFT, zorder=1))
        for r, letter in enumerate(seq):
            x = project(p[[i for i in m.residue(r + 1) if m.symbols[i] != 'H']].mean(0))[0]
            text(ax, x, y0 + 266, letter, size=32, bold=True, color=ACCENT if r == 1 else INK, ha='center')
        text(ax, 190, y0 + 302, f'threonine · {name} · threonine', size=23, color=MUTED, ha='center')
        text(ax, 446, y0 + 118, verb, size=23, color=MUTED, ha='center')
        arrow(ax, (398, y0 + 150), (494, y0 + 150), color=LINE, width=4)
        shot(ax, pt_crystal(shape, size), CRYSTAL_VIEWS[shape], (504, y0, 270, 300), 6.0, centre=(0, 0, 0))
        magnifier(ax, (846, y0 + 150), 66, '100' if shape == 'cube' else '111', color, scale=12.5)
        text(ax, 932, y0 + 104, shapes, size=34, bold=True, color=color)
        text(ax, 932, y0 + 152, f'{pattern} pattern of', size=24, color=BODY)
        text(ax, 932, y0 + 184, 'atoms on every face', size=24, color=BODY)
    return save(fig, 'hook')


def growth():
    """Slide 2's animation of the idea. A platinum cuboctahedron grows while TFT lying on its triangular faces slows
    them, so its square faces (tinted blue) grow out and vanish and it ends as an octahedron. It follows the rule in
    growth.py and is not a simulation from R13. Also saves the last frame as the still for print and for readers who
    ask for reduced motion. The loop starts again from the first frame, without a fade, which keeps the GIF small."""
    g = gr.Growth()
    final = g.atoms(gr.END)
    assert not g.on_square(final, gr.END).any(), 'the crystal should end as an octahedron, as slide 2 says'
    rotation = rt.view((0.75, -0.9, 0.35))
    size = 600  # px, a little above the 540 slide px it fills, which keeps the GIF under 3 MB
    seen = g.sites[final] * gr.UNIT @ rotation.T
    scale = (size / 2 - 14) / (np.abs(seen[:, :2]).max() + ELEMENTS['Pt'][1])
    ring = set(g.m.ring())
    colors = [ACCENT if i in ring else ELEMENTS['H'][0] if s == 'H' else BODY for i, s in enumerate(g.m.symbols)]
    metal, square = ELEMENTS['Pt'][0], mix(ELEMENTS['Pt'][0], BLUE, 0.45)
    frames = []
    for t in np.linspace(0, gr.END, 81):
        scene = rt.Scene()
        shown, outward = g.surface(g.atoms(t))
        front = outward @ rotation[2] > -0.3  # the far side is hidden anyway
        for site, blue in zip(g.sites[shown[front]] * gr.UNIT, g.on_square(shown[front], t)):
            scene.sphere(site, ELEMENTS['Pt'][1], square if blue else metal)
        for p in g.peptides:
            if gr.DIRECTIONS[p['face']] @ rotation[2] > -0.3 and (now := g.peptide_at(p, t)):
                ball_and_stick(scene, g.m.symbols, now[0], g.m.pairs, atom=1.6, bond=0.22, fade=0.8 * now[1],
                               colors=colors)
        picture, _ = rt.render(scene, rotation, size, size, scale, centre=(0, 0, 0), fog=0)
        frame = Image.new('RGB', picture.size, 'white')
        frame.paste(picture, mask=picture.getchannel('A'))
        frames.append(frame)
    frames[-1].save(ASSETS / 'growth-end.jpg', quality=92)
    return animate(frames, 'growth', [1000] + [80] * 79 + [1500])


def motivation():
    """Where what sticks to a surface matters: platinum crystals as catalysts (G18, R13), a gold rod for cancer
    treatment (G18), the bone-mineral-binding peptide SVSVGGK on hydroxyapatite's basal face (L16), and a grinding
    additive, triethanolamine, between two broken faces of tricalcium silicate (M13, EP2527307). Real lattices and
    molecules in illustrative arrangements."""
    fig, ax = canvas()
    tiles = (('Catalysts', ('Platinum crystals speed up', 'reactions. What sits on their',
                            'faces affects their shape and', 'how well they work.')),
             ('Medicine', ('Gold rods that turn light into', 'heat are studied for treating',
                           'cancer. Their surfaces interact', 'with water and biomolecules.')),
             ('Bones and teeth', ('Proteins steer how the mineral', 'of bones and teeth grows. That',
                                  'matters for osteoporosis and', 'tooth decay.')),
             ('Cement', ('Grinding is a big cost in making', 'cement. Additives that stick to',
                         'the grains stop them clumping,', 'so it takes less time and energy.')))
    for k, (head, lines) in enumerate(tiles):
        panel(ax, 436 * k, 0, 420, 654)
        text(ax, 436 * k + 30, 50, head, size=30, bold=True)
        for j, line in enumerate(lines):
            text(ax, 436 * k + 30, 94 + 31 * j, line, size=23, color=BODY)
    for shape, size, box in (('cube', 27.5, (24, 218, 240, 240)), ('tetra', 44.0, (176, 420, 240, 220))):
        shot(ax, pt_crystal(shape, size), CRYSTAL_VIEWS[shape], box, 5.4, centre=(0, 0, 0), background=TINT)
    gold = st.nanocrystal('Au', 'cube', 84).positions
    axis = np.clip(gold[:, 0], -30, 30)
    gold = gold[np.hypot(gold[:, 0] - axis, np.hypot(gold[:, 1], gold[:, 2])) <= 11.5]  # a rod 23 Å across
    scene = rt.Scene()
    spheres(scene, ['Au'] * len(gold), gold)
    shot(ax, scene, rt.view((0.25, -1, 0.5), (0.8, 0, 0.6)), (446, 214, 400, 430), 5.2, centre=(0, 0, 0),
         background=TINT)
    scene = rt.Scene()
    polyhedral(scene, *st.block(st.hydroxyapatite(), (4, 5, 1), (0, 0, 0), (28, 30, 6.8)), fade=0.3)
    m = st.Molecule(sequence='SVSVGGK', seed=5)
    p = m.extend()
    heavy = [i for i, s in enumerate(m.symbols) if s != 'H']
    centre = p[heavy].mean(0)
    p = (p - centre) @ np.linalg.svd(p[heavy] - centre)[2].T  # along the strand, across it, out of its plane
    ball_and_stick(scene, m.symbols, p + (14, 8, 10.6 - p[heavy, 2].min()), m.pairs, atom=1.3, bond=0.16)
    shot(ax, scene, front_view(50), (882, 214, 400, 430), 12.5, centre=(14, 15, 4), background=TINT)
    c3s = st.cod('1540704')
    scene = rt.Scene()
    for lo, hi, lift in (((0, 0, 0), (26, 18, 11), 0), ((0, 0, 14), (26, 18, 25), 8)):
        symbols, positions = st.block(c3s, (3, 3, 4), lo, hi)
        polyhedral(scene, symbols, positions + (0, 0, lift))
    for n, (x, y) in enumerate(((5, 6), (13, 5), (21, 6), (9, 13), (17, 14))):
        tea = st.Molecule('OCCN(CCO)CCO', seed=n + 1)
        q = tea.positions
        ball_and_stick(scene, tea.symbols, (q - q.mean(0)) @ st.rotation((1, n, 2), 1.1 * n + 0.4).T + (x, y, 16.5),
                       tea.pairs, atom=1.3, bond=0.16)
    shot(ax, scene, rt.view((0.2, -1, 0.15), (0, 0, 1)), (1318, 214, 400, 430), 10.0, centre=(13, 9, 16.5),
         background=TINT)
    return save(fig, 'motivation')


def compat():
    """Separately built metal and molecule models against IFF's shared equation and combination rules (K21)."""
    fig, ax = canvas()
    metal_icon, molecule_icon = pt_crystal('cube', 3 * st.LATTICE['Pt']), rt.Scene()
    m, p, _ = tripeptide('TFT')
    ball_and_stick(molecule_icon, m.symbols, p, m.pairs)
    for side, (title, color, link, rule, value, claim) in enumerate((
            ('Built separately', MUTED, False, ['No shared rule for', 'metal with molecules'],
             'Up to 50% low', ['surface energies in some of the', 'compared metal-only models']),
            ('Interface Force Field', ACCENT, True, ['So metal–molecule pairs', 'follow the same rules'],
             'Calibrated', ['to measured lattice size and', 'surface energy, with selected',
                            'interfaces tested separately']))):
        x0 = side * 894
        panel(ax, x0, 0, 834, 654, TINT)
        text(ax, x0 + 44, 52, title, size=32, bold=True, color=color)
        shot(ax, metal_icon, CRYSTAL_VIEWS['cube'], (x0 + 40, 88, 250, 204), 8.8, centre=(0, 0, 0))
        shot(ax, molecule_icon, FLAT, (x0 + 540, 88, 260, 204), 16)
        text(ax, x0 + 165, 318, 'Metal model', size=27, bold=True, ha='center')
        text(ax, x0 + 165, 354, 'its own equations' if not link else 'the molecules’ equations', size=24,
             color=BODY, ha='center')
        text(ax, x0 + 670, 318, 'Molecular model', size=27, bold=True, ha='center')
        text(ax, x0 + 670, 354, 'different equations' if not link else 'unchanged', size=24, color=BODY, ha='center')
        if link:
            ax.plot([x0 + 300, x0 + 530], [190, 190], color=ACCENT, lw=pt(5), zorder=3)
            ax.add_patch(Circle((x0 + 415, 190), 26, color=ACCENT, zorder=8))
            for dy in (-6.5, 6.5):  # an equals sign, the same rules, against the other panel's question mark
                ax.plot([x0 + 404, x0 + 426], [190 + dy, 190 + dy], color='white', lw=pt(5), zorder=9)
        else:
            dashed(ax, (x0 + 300, 190), (x0 + 380, 190), color=LINE, width=5)
            dashed(ax, (x0 + 450, 190), (x0 + 530, 190), color=LINE, width=5)
            ax.add_patch(Circle((x0 + 415, 190), 26, fc='white', ec=MUTED, lw=pt(3), zorder=8))
            text(ax, x0 + 415, 192, '?', size=30, bold=True, color=MUTED, ha='center', va='center_baseline', z=9)
        text(ax, x0 + 415, 414, rule[0], size=24, color=INK, ha='center')
        text(ax, x0 + 415, 446, rule[1], size=24, color=INK, ha='center')
        ax.plot([x0 + 44, x0 + 790], [500, 500], color=RULE, lw=pt(2), zorder=1)
        text(ax, x0 + 44, 566, value, size=44, bold=True, color=color)
        for j, line in enumerate(claim):
            text(ax, x0 + 400, 567 + (j - (len(claim) - 1) / 2) * 34, line, size=24, color=BODY)
    return save(fig, 'compat')


def catalog():
    """The solids IFF parameterizes, above the molecules it is combined with."""
    fig, ax = canvas()
    text(ax, 0, 14, 'SOLIDS AND THEIR SURFACES', size=18, bold=True, color=ACCENT)
    gold = st.nanocrystal('Au', 'cube', 5 * st.LATTICE['Au']).positions
    gold = gold[np.all(gold @ np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [-1, -1, -1], [-1, -1, 1],
                                        [-1, 1, -1], [1, -1, -1]]).T / np.sqrt(3) <= 11.0, axis=1)]
    scene = rt.Scene()
    spheres(scene, ['Au'] * len(gold), gold)
    shot(ax, scene, CRYSTAL_VIEWS['cube'], (0, 42, 400, 250), 7.6, centre=(0, 0, 0))
    scene = rt.Scene()
    polyhedral(scene, *st.silica((8, 8, 3), (2, 8, 2.5), (24, 22, 14)))
    shot(ax, scene, rt.view((0.3, -1, 0.45)), (442, 42, 400, 250), 12.6)
    scene = rt.Scene()
    polyhedral(scene, *st.block(st.hydroxyapatite(), (4, 4, 2), (0, 0, 0), (28, 22, 7.0)))
    shot(ax, scene, rt.view((0.15, -0.25, 1), (0, 1, 0)), (884, 42, 400, 250), 9.6)
    scene = rt.Scene()
    polyhedral(scene, *st.block(st.cod('1540704'), (3, 2, 3), (0, 0, 0), (30, 7.5, 21)))
    shot(ax, scene, rt.view((0.12, -1, 0.15)), (1326, 42, 400, 250), 9.4)
    for x, head, line in ((0, 'Metals', 'gold, platinum and other metals'),
                          (442, 'Silica', 'sand and glass, with OH groups'),
                          (884, 'Hydroxyapatite', 'the mineral in bone and teeth'),
                          (1326, 'Cement', 'tricalcium silicate')):
        text(ax, x + 200, 314, head, size=28, bold=True, ha='center')
        text(ax, x + 200, 350, line, size=23, color=MUTED, ha='center')
    text(ax, 0, 410, 'COMBINED WITH STANDARD MOLECULE MODELS SUCH AS AMBER, CHARMM, OPLS-AA AND PCFF', size=18,
         bold=True, color=TEAL)
    sym, pos = st.water_box((-11, -5, -4), (11, 5, 4), seed=2)
    drop = np.repeat(np.sum((pos[::3] / (11, 5, 4)) ** 2, axis=1) < 1, 3)  # a rounded droplet of liquid water
    scene = rt.Scene()
    ball_and_stick(scene, [e for e, k in zip(sym, drop) if k], pos[drop])
    shot(ax, scene, FLAT, (0, 436, 540, 160), 14.4)
    m, flat_pose, _ = st.s7()
    scene = rt.Scene()
    ball_and_stick(scene, m.symbols, flat_pose, m.pairs)
    shot(ax, scene, FLAT, (594, 436, 540, 160), 13)
    m, chain = polyethylene()
    scene = rt.Scene()
    ball_and_stick(scene, m.symbols, chain, m.pairs)
    shot(ax, scene, rt.view((0, -0.3, 1), (0, 1, 0)), (1188, 436, 540, 160), 19.5)
    for x, head in ((0, 'Water'), (594, 'Peptides and proteins'), (1188, 'Polymers')):
        text(ax, x + 270, 624, head, size=28, bold=True, ha='center')
    return save(fig, 'catalog')


FIGURES = (cover, hook, growth, motivation, compat, catalog)
