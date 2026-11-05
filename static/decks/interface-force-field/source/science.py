#!/usr/bin/env python3
"""The deck's worked numbers, computed from cited published parameters and checked.

`python science.py` writes data/science-checks.json and data/lj-curves.csv. The checks verify
algebra and arithmetic, not the accuracy of a physical model; no material trajectory is run here.
"""
import csv
import json

import numpy as np

from style import DATA, SOURCE

PARAMETERS = json.loads((SOURCE / 'parameters.json').read_text())
METALS = {k: (v['r0_A'], v['epsilon_kcal_mol']) for k, v in PARAMETERS['metals'].items()}
RH_9_6 = (PARAMETERS['metals_9_6']['Rh']['r0_A'], PARAMETERS['metals_9_6']['Rh']['epsilon_kcal_mol'])
COULOMB = PARAMETERS['coulomb']['constant_rounded_kcal_A_mol_e2']  # kcal Å mol⁻¹ e⁻²
RH_LATTICE = 3.8032  # Å, K21 Table 2: the five-cell edge 19.016 Å divided by 5


def energy(r, r0, epsilon):
    """12-6 Lennard-Jones pair energy (kcal/mol) with its minimum -epsilon at r0 (K21 Eq. 1)."""
    x = r0 / np.asarray(r, float)
    return epsilon * (x ** 12 - 2 * x ** 6)


def force(r, r0, epsilon):
    """Radial force -dU/dr (kcal/mol/Å); positive pushes the two atoms apart."""
    x = r0 / np.asarray(r, float)
    return 12 * epsilon / np.asarray(r, float) * (x ** 12 - x ** 6)


def energy_9_6(r, r0, epsilon):
    """9-6 Lennard-Jones pair energy (kcal/mol) with its minimum -epsilon at r0 (K21 Eq. 2)."""
    x = r0 / np.asarray(r, float)
    return epsilon * (2 * x ** 9 - 3 * x ** 6)


def mixed(a, b):
    """The geometric-mean rule for an unlike pair, (r0, epsilon) from two like pairs (CVFF, as used in K21)."""
    return float(np.sqrt(a[0] * b[0])), float(np.sqrt(a[1] * b[1]))


def misread(r0, epsilon):
    """The (r0, epsilon) of the curve a program expecting the zero crossing sigma draws when given r0 instead."""
    return r0 * 2 ** (1 / 6), epsilon


def coulomb(r, qi=1, qj=-1):
    """Coulomb energy (kcal/mol) of two point charges in elementary charges, in vacuum."""
    return COULOMB * qi * qj / np.asarray(r, float)


def checks():
    h = 1e-5
    for r0, eps in [*METALS.values(), RH_9_6]:
        sigma = r0 / 2 ** (1 / 6)
        for d in np.linspace(r0 * 0.87, r0 * 2, 25):
            slope = (energy(d + h, r0, eps) - energy(d - h, r0, eps)) / (2 * h)
            np.testing.assert_allclose(force(d, r0, eps), -slope, rtol=1e-7, atol=1e-8)
            np.testing.assert_allclose(energy(d, r0, eps), 4 * eps * ((sigma / d) ** 12 - (sigma / d) ** 6), rtol=1e-12)
        assert np.isclose(energy(r0, r0, eps), -eps) and abs(force(r0, r0, eps)) < 1e-10
        assert np.isclose(energy_9_6(r0, r0, eps), -eps)
        assert abs(energy_9_6(r0 + h, r0, eps) - energy_9_6(r0 - h, r0, eps)) < 1e-8
    rh, ca = METALS['Rh'], METALS['Ca']
    rh_ca = mixed(rh, ca)
    wrong = misread(*rh)
    for d in np.linspace(2.3, 8, 25):  # the textbook form with sigma = 2.757 Å is the misread curve
        np.testing.assert_allclose(energy(d, *wrong), 4 * rh[1] * ((rh[0] / d) ** 12 - (rh[0] / d) ** 6), rtol=1e-12)
    a = RH_LATTICE
    corner, face = 8 * (1 / 8), 6 * (1 / 2)
    k12, k96 = (PARAMETERS['rhodium_evidence']['bulk_modulus_GPa'][k] for k in ('LJ12_6', 'LJ9_6'))
    k_exp = PARAMETERS['rhodium_evidence']['bulk_modulus_GPa']['experiment_selected']
    out = {
        'status': 'algebra and arithmetic checks passed; no new material validation',
        'Rh_sigma_zero_crossing_A': rh[0] / 2 ** (1 / 6),
        'Rh_points': [{'distance_A': d, 'energy_kcal_mol': float(energy(d, *rh)),
                       'radial_force_kcal_mol_A': float(force(d, *rh))} for d in (2.4, 2.5, rh[0], 3.0, 4.2, 10.0)],
        'Rh_9_6': {'r0_A': RH_9_6[0], 'epsilon_kcal_mol': RH_9_6[1]},
        'Rh_Ca_geometric_pair': {'r0_A': rh_ca[0], 'epsilon_kcal_mol': rh_ca[1],
                                 'energy_at_4A_kcal_mol': float(energy(4.0, *rh_ca))},
        'Rh_r0_read_as_sigma': {'minimum_A': wrong[0], 'energy_at_2_757A_kcal_mol': float(energy(rh[0], *wrong)),
                                'length_scale': wrong[0] / rh[0]},
        'coulomb_unit_charges_vacuum_kcal_mol': {'3A': float(coulomb(3.0)), '10A': float(coulomb(10.0))},
        'three_atom_triangle_at_r0_kcal_mol': 3 * float(energy(rh[0], *rh)),
        'Rh_fcc': {'lattice_A': a, 'nearest_neighbour_A': a / np.sqrt(2), 'neighbours': 12,
                   'atoms_per_cell': corner + face, 'five_cell_edge_A': 5 * a, 'five_cell_atoms': 4 * 5 ** 3},
        'Rh_bulk_modulus_deviation_percent': {'LJ12_6': (k12 / k_exp - 1) * 100, 'LJ9_6': (k96 / k_exp - 1) * 100},
    }
    assert np.isclose(out['Rh_sigma_zero_crossing_A'], 2.4562, atol=5e-5)
    assert np.allclose([p['energy_kcal_mol'] for p in out['Rh_points'][1:4]], [-2.838, -7.84, -6.601], atol=5e-4)
    assert np.allclose([p['radial_force_kcal_mol_A'] for p in out['Rh_points'][1:4]], [54.072, 0, -7.511], atol=5e-4)
    assert np.allclose([rh_ca[0], rh_ca[1], out['Rh_Ca_geometric_pair']['energy_at_4A_kcal_mol']],
                       [3.3312, 5.1325, -2.8533], atol=5e-5)
    assert np.isclose(wrong[0], 3.0946, atol=5e-5) and abs(energy(rh[0], *wrong)) < 1e-12
    assert np.isclose(out['coulomb_unit_charges_vacuum_kcal_mol']['3A'], -110.688, atol=5e-4)
    assert np.isclose(out['three_atom_triangle_at_r0_kcal_mol'], -23.52)
    assert np.isclose(out['Rh_fcc']['nearest_neighbour_A'], 2.6893, atol=5e-5) and corner + face == 4
    assert np.isclose(5 * a, PARAMETERS['rhodium_evidence']['five_cell_lattice_A']['experiment'])
    assert np.isclose(out['Rh_bulk_modulus_deviation_percent']['LJ12_6'], -6.52, atol=5e-3)
    return out


def main():
    out = checks()
    DATA.mkdir(exist_ok=True)
    (DATA / 'science-checks.json').write_text(json.dumps(out, indent=2) + '\n')
    with (DATA / 'lj-curves.csv').open('w', newline='') as handle:
        writer = csv.writer(handle, lineterminator='\n')
        writer.writerow(['metal', 'r_A', 'U_kcal_mol_pairs', 'F_radial_kcal_mol_A'])
        for metal, (r0, eps) in METALS.items():
            for d in np.linspace(r0 * 0.85, 8, 700):
                writer.writerow([metal, float(d), float(energy(d, r0, eps)), float(force(d, r0, eps))])
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
