"""Rebuild original educational IFF plots from cited published parameters.

Run with Python, numpy and matplotlib. No material trajectories are calculated.
The checks verify algebra and arithmetic, not accuracy of a physical model.
"""

import csv
import json
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


SOURCE = Path(__file__).resolve().parent
ASSETS = SOURCE.parent / "assets"
DATA = SOURCE / "data"
PARAMETERS = json.loads((SOURCE / "parameters.json").read_text())
METALS = PARAMETERS["metals"]
COLORS = {"Rh": "#1D7F79", "Ir": "#3474B8", "Ca": "#B3263E", "Sr": "#667788"}
INK = "#172332"
PAPER = "#ffffff"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 17,
    "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": "#a9b0b5",
    "xtick.color": INK, "ytick.color": INK, "axes.spines.top": False,
    "axes.spines.right": False, "axes.facecolor": PAPER,
    "figure.facecolor": PAPER, "axes.titleweight": "bold",
    "svg.fonttype": "none", "svg.hashsalt": "iff-original-plots-v1",
})


def energy(r, r0, epsilon):
    x = r0 / np.asarray(r)
    return epsilon * (x**12 - 2 * x**6)


def force(r, r0, epsilon):
    x = r0 / np.asarray(r)
    return 12 * epsilon / np.asarray(r) * (x**12 - x**6)


def save(fig, name):
    fig.savefig(ASSETS / f"{name}.png", dpi=160, metadata={"Software": "Sean Florez"})
    fig.savefig(ASSETS / f"{name}.svg", metadata={"Creator": "Sean Florez", "Date": None})
    plt.close(fig)


def axes(title, ylabel, xlim, ylim):
    fig, ax = plt.subplots(figsize=(11.6, 6.3), layout="constrained")
    ax.set(title=title, xlabel="Atom separation r (Å)", ylabel=ylabel, xlim=xlim, ylim=ylim)
    ax.axhline(0, color="#919aa2", lw=1)
    ax.grid(alpha=0.13)
    return fig, ax


def source_line(fig, text="Analytical illustration from Kanhaiya et al. (2021), Eq. 1 and Table 1. Not a trajectory."):
    fig.supxlabel(text, fontsize=11, color="#56616b")


def main():
    ASSETS.mkdir(exist_ok=True)
    DATA.mkdir(exist_ok=True)
    rh = METALS["Rh"]
    r0, epsilon = rh["r0_A"], rh["epsilon_kcal_mol"]
    sigma = r0 / 2**(1 / 6)
    r = np.linspace(2.35, 6.2, 1000)

    fig, ax = axes("Rhodium: energy of one pair", "Energy U (kcal/mol of pairs)", (2.35, 6.2), (-10.5, 14))
    ax.plot(r, energy(r, r0, epsilon), color=COLORS["Rh"], lw=3.5)
    ax.axvline(sigma, color=COLORS["Ca"], ls=":", lw=1.5)
    ax.axvline(r0, color=COLORS["Rh"], ls=":", lw=1.5)
    ax.scatter([sigma, r0, 3.0], [0, -epsilon, energy(3.0, r0, epsilon)], color=INK, s=32, zorder=5)
    ax.annotate("σ = 2.456 Å\nzero energy", (sigma, 0), (3.3, 7.2), arrowprops={"arrowstyle": "->", "color": INK})
    ax.annotate("r₀ = 2.757 Å\nlowest pair energy", (r0, -epsilon), (3.5, -5.0), arrowprops={"arrowstyle": "->", "color": INK})
    ax.annotate("", (5.45, 0), (5.45, -epsilon), arrowprops={"arrowstyle": "<->", "color": COLORS["Rh"], "lw": 2})
    ax.text(5.55, -4.2, "ε = 7.84\nkcal/mol", va="center", fontsize=15)
    ax.text(2.41, 11.3, "Too close", fontsize=15)
    ax.text(4.25, 1.2, "Far apart: U approaches zero", fontsize=15)
    source_line(fig)
    save(fig, "lj-energy")

    fig, ax = axes("Rhodium: force is the negative energy slope", "Radial force (kcal/mol/Å)", (2.35, 6.2), (-13, 90))
    ax.plot(r, force(r, r0, epsilon), color=COLORS["Rh"], lw=3.5)
    ax.axvline(r0, color=COLORS["Rh"], ls=":", lw=1.5)
    ax.scatter([r0], [0], color=INK, s=40, zorder=5)
    ax.annotate("At r₀: force = 0", (r0, 0), (3.6, 19), arrowprops={"arrowstyle": "->", "color": INK})
    ax.text(2.62, 63, "Positive force\npushes atoms apart", fontsize=18)
    ax.text(3.55, -10.8, "Negative force pulls atoms together", fontsize=16)
    source_line(fig)
    save(fig, "lj-force")

    fig, axs = plt.subplots(1, 2, figsize=(14, 6.1), layout="constrained")
    rr = np.linspace(2.3, 7.4, 1600)
    for metal, p in METALS.items():
        label = f"{metal}  r₀ {p['r0_A']:.3f} Å; ε {p['epsilon_kcal_mol']:.2f}"
        axs[0].plot(rr, energy(rr, p["r0_A"], p["epsilon_kcal_mol"]), color=COLORS[metal], lw=2.7, label=label)
        axs[1].plot(rr, force(rr, p["r0_A"], p["epsilon_kcal_mol"]), color=COLORS[metal], lw=2.7, label=metal)
    for ax in axs:
        ax.set_xlim(2.3, 7.4)
        ax.set_xlabel("Separation r (Å)")
        ax.axhline(0, color="#919aa2", lw=1)
        ax.grid(alpha=0.13)
    axs[0].set(title="Energy curves", ylabel="Energy (kcal/mol)", ylim=(-11, 14))
    axs[1].set(title="Force curves", ylabel="Radial force (kcal/mol/Å)", ylim=(-15, 70))
    axs[0].legend(fontsize=11, loc="upper right", frameon=False)
    axs[1].legend(fontsize=12, loc="upper right", frameon=False)
    source_line(fig, "Kanhaiya et al. (2021), Table 1, p. 3. Curves are clipped at the upper plot boundary; no physical cutoff is applied.")
    save(fig, "lj-metals")

    ca = METALS["Ca"]
    mixed_r0 = np.sqrt(r0 * ca["r0_A"])
    mixed_epsilon = np.sqrt(epsilon * ca["epsilon_kcal_mol"])
    fig, ax = axes("A different-element pair needs a combining rule", "Energy (kcal/mol of pairs)", (2.35, 7.1), (-11, 13))
    rr = np.linspace(2.35, 7.1, 1200)
    for label, a, b, color, ls in [
        ("Rh–Rh", r0, epsilon, COLORS["Rh"], "--"),
        ("Ca–Ca", ca["r0_A"], ca["epsilon_kcal_mol"], COLORS["Ca"], "--"),
        ("Rh–Ca, geometric rule", mixed_r0, mixed_epsilon, INK, "-"),
    ]:
        ax.plot(rr, energy(rr, a, b), color=color, lw=3, ls=ls, label=label)
    ax.legend(fontsize=14, loc="upper right", frameon=False)
    ax.text(4.15, -6.4, f"r₀,ij = √(r₀,i r₀,j) = {mixed_r0:.3f} Å\nεᵢⱼ = √(εᵢ εⱼ) = {mixed_epsilon:.3f} kcal/mol", fontsize=15)
    source_line(fig, "Explicit CVFF geometric convention. Arithmetic radii apply in other families. This is not validation of a Rh–Ca alloy.")
    save(fig, "pair-mixing")

    k = PARAMETERS["coulomb"]["constant_rounded_kcal_A_mol_e2"]
    fig, ax = axes("Charged atoms add a Coulomb interaction", "Coulomb energy (kcal/mol of pairs)", (2, 10), (-180, 180))
    rr = np.linspace(2, 10, 600)
    ax.plot(rr, -k / rr, color=COLORS["Rh"], lw=3, label="+1e and −1e: attraction")
    ax.plot(rr, k / rr, color=COLORS["Ca"], lw=3, label="+1e and +1e: repulsion")
    ax.scatter([3], [-k / 3], color=INK, s=40, zorder=5)
    ax.annotate(f"At 3 Å: −{k / 3:.2f} kcal/mol", (3, -k / 3), (4.3, -150), arrowprops={"arrowstyle": "->", "color": INK}, fontsize=16)
    ax.text(5.1, 22, "U = k qᵢqⱼ / r", fontsize=20)
    ax.legend(fontsize=14, loc="upper right", frameon=False)
    source_line(fig, "Illustrative point charges in vacuum, not Rh charges. Solvent, screening and periodic boundaries are absent.")
    save(fig, "charged-pair")

    points = np.array([[0.0, 0.0], [r0, 0.0], [r0 / 2, r0 * np.sqrt(3) / 2]])
    pair_rows = []
    for i, j in combinations(range(3), 2):
        d = float(np.linalg.norm(points[j] - points[i]))
        pair_rows.append({"i": i + 1, "j": j + 1, "distance_A": d, "energy_kcal_mol": float(energy(d, r0, epsilon))})
    cluster_energy = sum(p["energy_kcal_mol"] for p in pair_rows)
    fig, ax = plt.subplots(figsize=(11.6, 6.3), layout="constrained")
    for p in pair_rows:
        a, b = points[p["i"] - 1], points[p["j"] - 1]
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#919aa2", ls=":", lw=2)
    # Sphere diameter equals the pair minimum in this illustrative geometry.
    for i, p in enumerate(points):
        ax.add_patch(Circle(p, r0 / 2, facecolor=COLORS["Rh"], edgecolor=PAPER, lw=2, alpha=0.92, zorder=3))
        ax.text(*p, str(i + 1), color="white", fontsize=23, ha="center", va="center", zorder=4)
    ax.text(5.3, 3.3, "3 atoms → 3 distinct pairs", fontsize=23, weight="bold")
    ax.text(5.3, 2.3, f"Every separation is r₀ = {r0:.3f} Å", fontsize=19)
    ax.text(5.3, 1.3, f"Each pair: {pair_rows[0]['energy_kcal_mol']:.2f} kcal/mol", fontsize=19)
    ax.text(5.3, -0.3, f"Utotal = U₁₂ + U₁₃ + U₂₃\n= {cluster_energy:.2f} kcal/mol of clusters", fontsize=21, linespacing=1.6)
    ax.set(xlim=(-1.8, 13.5), ylim=(-1.8, 4.5), aspect="equal", title="A tiny cluster adds its pair energies")
    ax.axis("off")
    source_line(fig, "Illustrative pair-minimum geometry. Sphere diameter = r₀. No cluster relaxation or stability prediction; not an fcc crystal.")
    save(fig, "cluster-sum")

    fig, axs = plt.subplots(1, 2, figsize=(12.8, 6.3), layout="constrained")
    axs[0].bar([0, 1, 2], [2.64, 2.643, 2.643], color=["#adb5bb", COLORS["Rh"], COLORS["Ca"]], width=0.6)
    axs[0].errorbar([0], [2.64], yerr=[0.02], color=INK, capsize=5, fmt="none")
    axs[1].bar([0, 1, 2], [276, 258, 175], color=["#adb5bb", COLORS["Rh"], COLORS["Ca"]], width=0.6)
    for ax, vals in zip(axs, [[2.64, 2.643, 2.643], [276, 258, 175]]):
        ax.set_xticks([0, 1, 2], ["Experiment", "12–6 LJ", "9–6 LJ"], fontsize=13)
        ax.grid(axis="y", alpha=0.13)
        for i, val in enumerate(vals):
            ax.text(i, val * 1.04, str(val), ha="center", fontsize=16)
    axs[0].set(title="Fitted surface energy", ylabel="Rh(111) surface energy (J/m²)", ylim=(0, 3.3))
    axs[1].set(title="Independent bulk modulus", ylabel="Bulk modulus (GPa)", ylim=(0, 350))
    source_line(fig, "Kanhaiya et al. (2021), Tables 3 and 5. Experimental K=276 GPa is selected reference d; other entries are 269–271 GPa.")
    save(fig, "rh-evidence")

    checks = []
    rows = []
    for metal, p in METALS.items():
        a, b = p["r0_A"], p["epsilon_kcal_mol"]
        s = a / 2**(1 / 6)
        assert np.isclose(energy(a, a, b), -b)
        assert abs(force(a, a, b)) < 1e-10
        assert abs(energy(s, a, b)) < 1e-10
        for d in np.linspace(a * 0.87, a * 2, 25):
            h = 1e-5
            finite_difference = -(energy(d + h, a, b) - energy(d - h, a, b)) / (2 * h)
            np.testing.assert_allclose(force(d, a, b), finite_difference, rtol=1e-7, atol=1e-8)
            conventional = 4 * b * ((s / d)**12 - (s / d)**6)
            np.testing.assert_allclose(energy(d, a, b), conventional, rtol=1e-12, atol=1e-10)
        checks.append({"metal": metal, "r0_A": a, "epsilon_kcal_mol": b, "sigma_zero_A": s, "minimum_and_derivative_checks": "pass"})
        for d in np.linspace(a * 0.85, 8, 700):
            rows.append([metal, float(d), float(energy(d, a, b)), float(force(d, a, b))])
    assert len(pair_rows) == 3 and np.isclose(cluster_energy, -3 * epsilon)
    assert force(r0 * 0.9, r0, epsilon) > 0 > force(r0 * 1.1, r0, epsilon)
    results = {
        "status": "algebra and numeric checks passed; no new material validation",
        "parameters": checks,
        "Rh_worked_examples": [{"distance_A": d, "energy_kcal_mol": float(energy(d, r0, epsilon)), "radial_force_kcal_mol_A": float(force(d, r0, epsilon))} for d in [2.5, r0, 3.0, 4.0]],
        "Rh_Ca_geometric_pair": {"r0_A": float(mixed_r0), "epsilon_kcal_mol": float(mixed_epsilon), "energy_at_4A_kcal_mol": float(energy(4, mixed_r0, mixed_epsilon))},
        "coulomb_opposite_unit_charges_vacuum_at_3A_kcal_mol": -k / 3,
        "cluster": {"pairs": pair_rows, "total_energy_kcal_mol_of_clusters": cluster_energy},
        "Rh_bulk_modulus_deviation_percent": {"LJ12_6": (258 / 276 - 1) * 100, "LJ9_6": (175 / 276 - 1) * 100},
        "surface_note": "epsilon is a pair well depth; gamma is energy per area from many interactions. They have different units.",
    }
    (DATA / "science-checks.json").write_text(json.dumps(results, indent=2) + "\n")
    with (DATA / "lj-curves.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metal", "r_A", "U_kcal_mol_pairs", "F_radial_kcal_mol_A"])
        writer.writerows(rows)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
