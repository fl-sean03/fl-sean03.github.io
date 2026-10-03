"""Write the presentation's public citation, evidence and asset manifest."""
from pathlib import Path
import hashlib
import json

from story import SL, SOURCES

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "website-bundle"

ROLES = {
    1: "explanation", 2: "question definition", 3: "workflow explanation",
    4: "source-derived ideal geometry", 5: "source-derived ideal geometry",
    6: "source-derived ideal geometry", 7: "model definition", 8: "method taxonomy",
    9: "model definition", 10: "published parameter set",
    11: "analytical convention conversion", 12: "analytical illustration",
    13: "schematic", 14: "illustrative motion", 15: "estimator definitions",
    16: "published estimator / constructed visual", 17: "comparison conditions",
    18: "calibration agreement", 19: "non-fitted property comparison",
    20: "binary-alloy chemical example", 21: "charge-hypothesis sensitivity; raw energies",
    22: "fit / validation separation",
    23: "hypothetical revision contract plus published data",
    24: "documented workflow", 25: "human decision gates",
    26: "illustrative input/output contract", 27: "generic scientific acceptance requirements",
    28: "method role comparison", 29: "proposed full loop",
    30: "workflow inputs and outputs", 31: "analytical equations",
    32: "published calibration and non-fitted property data",
    33: "uncertainty categories", 34: "bibliography", 35: "reuse and limitations",
}
LOCATORS = {
    "K21": "Table 1 (parameters); Table 2 (lattice); Table 3 (surface); Table 5 (mechanics); SI S3–S8 (methods)",
    "K21C": "Author correction; corrected supplementary archive, METAL_UNIT_CELLS_AND_SURFACE_MODELS/rh_*",
    "L18SI": "Original Supporting Information S15–S19, Tables S1–S2",
    "L18": "Publisher SI record and original SI; main-paper numeric results excluded",
    "LJ": "lj/cut formula and sigma convention",
    "MD": "NVE velocity-Verlet and minimization documentation",
    "MACE": "Primary MACE paper introduction/method",
    "AGENT": "IFF Agent workflow documentation (2026)",
    "DERIVED": "Original calculations and labeled illustrations",
}
claims = []
for slide in SL:
    number = slide["id"]
    units = ""
    state = "Not a numerical material result"
    model = "Explanation only"
    if number in (4, 5, 6):
        units = "Å; atom count"
        state = "Static ideal source-derived geometry, a=3.8032 Å"
        model = "Rh fcc Fm-3m, corrected 2021 supplementary dataset"
    if number in (10, 11, 12, 14, 31):
        units = "Å, kcal/mol; reduced U/epsilon and Fr*Rmin/epsilon where labeled"
        model = "K21 12-6 / 9-6 conventions; illustrative analytical model"
        state = "Pair illustration, not material trajectory"
    if number in (18, 19, 32):
        units = "5a in Å; gamma in J/m²; K in GPa"
        state = "Published lattice/surface at 298 K and atmospheric lattice pressure; mechanical procedure SI S6–S8"
        model = "Published K21 12-6 and 9-6 parameter sets, no refit here"
    if number in (20, 21):
        units = "e (fractional charge); eV (raw defect energy)"
        state = "Liu SI AlNi charge/defect examples; no new fitted geometry or trajectory"
        model = "L18 SI Table S2 base +/-0.39e with stated alternative charge distributions"
    uncertainty = "Only reported experimental uncertainties plotted; no invented simulation error bars"
    if number in (19, 32, 33):
        uncertainty += ". SI S7-S8 mechanical repeatability approximately +/-3% is protocol agreement, not accuracy or a statistical interval."
    claims.append({
        "slide": number, "title": slide["title"],
        "claims": [slide["lead"]] + [str(item) for item in slide["items"]],
        "classification": ROLES[number], "source_ids": slide["refs"],
        "locators": {source: LOCATORS[source] for source in slide["refs"]},
        "model_revision": model, "conditions": state, "units": units,
        "calibration_validation": ROLES[number], "uncertainty": uncertainty,
        "notes": slide["notes"],
        "permission_reuse": "Original diagrams/plots, attributed facts; no third-party source figures or PDFs distributed; no additional reuse license granted for original assets",
    })

assets = []
files = [(p, Path("media") / p.name) for p in (BUNDLE / "media").glob("*")]
files += [(p, Path("source/data") / p.name) for p in (ROOT / "data").glob("*")]
for path, public_path in sorted(files, key=lambda item: str(item[1])):
    if not path.is_file():
        continue
    stem = path.stem
    sources = ["DERIVED"]
    role = "original illustrative asset"
    state = "No new scientific simulation"
    units = "see asset labels"
    revision = "original deterministic production"
    if stem.startswith(("rh", "structure")):
        sources = ["K21", "K21C"]
        role = "source-derived ideal atomic geometry / original render"
        state = "Rh fcc a=3.8032 Å; slab is constructed, not research trajectory"
        units = "Å"
        revision = "corrected 2021 supplementary geometry"
    if stem.startswith(("calibration", "bulk", "published", "evidence")):
        sources = ["K21"]
        role = "original replot/reveal of published numerical results"
        state = "Tables 2,3,5 and SI conditions; not rerun"
        units = "Å, J/m², GPa"
        revision = "published 12-6 / 9-6 models"
    if stem.startswith("alloy"):
        sources = ["L18SI"]
        role = "original replot of factual raw-energy table entries"
        state = "AlNi Ni-vacancy charge hypotheses, SI Table S2"
        units = "eV"
        revision = "L18 SI Table S2"
    if stem.startswith(("energy", "model", "lj-")):
        sources = ["K21", "DERIVED"]
        role = "analytical pair illustration / prescribed motion"
        state = "Reduced units; not a material trajectory"
        units = "r/Rmin, U/epsilon, Fr Rmin/epsilon"
        revision = "analytical 12-6 Rmin convention"
    if stem == "rh-parameters":
        sources = ["K21"]
        role = "published parameter table transcription"
        state = "Table 1 Rh, neutral elemental-metal LJ model"
        units = "Å, kcal/mol"
        revision = "Published K21 12-6 and 9-6 models"
    if stem == "rh-validation":
        sources = ["K21"]
        role = "original replot of non-fitted bulk modulus predictions"
        state = "Rh, Table 5 selected 276 GPa experimental reference"
        units = "GPa"
        revision = "Published K21 12-6 and 9-6 models"
    if stem == "geometry":
        sources = ["K21", "K21C"]
        role = "source-derived geometry provenance"
        state = "Static ideal Rh cell and constructed slab"
        units = "Å, atom count"
        revision = "corrected 2021 supplementary geometry"
    license_text = "CC BY 4.0 (source asset)" if path.suffix == ".car" else "No additional reuse license granted for original authoring assets; third-party source attribution retained"
    reuse_notes = "L18 SI itself is CC BY-NC 4.0; source PDFs and figures are excluded. This asset newly draws table facts." if "L18SI" in sources else "Preserve attribution and identify source-derived constructions; no additional license is granted for original assets."
    assets.append({
        "path": public_path.as_posix(), "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "source_ids": sources,
        "model_revision": revision, "conditions": state, "units": units,
        "role": role, "license": license_text, "reuse_notes": reuse_notes,
    })

manifest = {
    "schema": "iff-showcase.citation-license/v1", "prepared": "2026-10-03",
    "scope": "Public educational presentation and reproducible source",
    "scientific_status": "Published results not rerun; no newly fitted, validated or adopted package",
    "sources": SOURCES, "claims": claims, "assets": assets,
    "fonts": [
        {"family": "Lato", "license": "SIL Open Font License 1.1", "use": "Native deck text; PDF/SVG glyph export, no font files distributed"},
        {"family": "DejaVu Sans", "license": "DejaVu fonts license", "use": "Original plots and raster media; no font files distributed"},
    ],
    "scientific_and_compatibility_limits": [
        "The alloy example uses original Liu SI numerical results; main-paper numerical results are excluded.",
        "No new material MD, experimental work or parameter fitting was performed for this presentation.",
    ],
}
BUNDLE.mkdir(exist_ok=True)
output = BUNDLE / "citation-license-manifest.json"
output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
print(output.name)
