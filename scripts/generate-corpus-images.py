#!/usr/bin/env python3
"""
Generate header images for the Territorial Engineering research corpus using
OpenAI gpt-image-2. API key is loaded from ~/.secrets/openai-api-key.

Each article gets a 1536x1024 header. Images are saved to
static/images/research/territorial-engineering/.

Run with --only <slug> to regenerate a single image. Run with --dry-run to
print the prompts without hitting the API.
"""

import argparse
import base64
import sys
import time
from pathlib import Path

from openai import OpenAI

KEY_PATH = Path("~/.secrets/openai-api-key").expanduser()
OUT_DIR = Path(
    "/home/sfhs1/Workspace/personal-site/static/images/research/territorial-engineering"
)

STYLE = (
    "Photorealistic, cinematic satellite-and-engineering aesthetic. "
    "Muted palette: deep navy, slate, steel gray, warm sodium-orange accents. "
    "High detail, high contrast, no text, no captions, no watermarks, no people. "
    "Composition works as a wide 3:2 article header."
)

PROMPTS = {
    "ontology": (
        "A conceptual diagram-as-photograph: a massive dredged coastal fill site "
        "seen from high aerial angle, with the geometry of cell perimeters, bund "
        "walls, and reclamation phases visible as distinct ordered regions. The "
        "water is deep blue-black, the fill is warm tan, the engineering works "
        "read as a taxonomy of forms. Evokes the idea of categorizing types of "
        "new land. " + STYLE
    ),
    "coastal-morphodynamics": (
        "Aerial view of a long sandy barrier island coastline at dusk, with "
        "visible longshore sediment transport patterns: sandbars, tombolos, "
        "breaking waves arriving obliquely to the shore. Subtle vector-like "
        "current traces across the water. The land is narrow and ribbon-like. "
        "Evokes physics of sediment in motion. " + STYLE
    ),
    "sediment-as-infrastructure": (
        "A massive trailing suction hopper dredger photographed from a low aerial "
        "angle at working depth, its drag arm deployed to the seabed, a plume of "
        "sediment trailing behind. The vessel is industrial and purposeful. Late "
        "afternoon light, deep blue water, steel hull. Evokes sand as a supply "
        "chain. " + STYLE
    ),
    "storm-surge-and-sea-level": (
        "A dark satellite-style image of a hurricane spiraling off a low-lying "
        "coast at night, with a sliver of illuminated city grid along the "
        "shoreline visible through gaps in the cloud. Storm is immense, city is "
        "small. Mood is tension, not destruction. " + STYLE
    ),
    "reclamation-methods": (
        "Construction site view of a hydraulic fill operation: a pipeline "
        "discharging a slurry of sand and water onto a growing fill cell, bund "
        "walls visible, water contained inside the cell decanting out through a "
        "weir. Bulldozers working the edge. Industrial scale, clear ordered "
        "process, mid-day light. " + STYLE
    ),
    "engineering-with-nature": (
        "A restored barrier island from low aerial angle, with new dune "
        "vegetation catching late afternoon light, gentle wave breaking on a "
        "broad beach, a marsh edge on the landward side. Engineered but "
        "vegetated, ecological but built. Soft warm tones, no hard edges. " + STYLE
    ),
    "industrial-base": (
        "A shipyard scene at dusk with multiple massive dredging vessels under "
        "construction or outfitting, cranes silhouetted against a red-orange "
        "sky, lights reflecting on oily harbor water. Industrial capacity made "
        "visible. " + STYLE
    ),
    "global-precedents": (
        "A high-altitude composite aerial view of an engineered coastline city: "
        "orthogonal reclaimed blocks extending into dark water, a visible "
        "boundary between original shoreline and reclaimed fill, dense urban "
        "pattern on the new land. Evokes Singapore or Tokyo Bay seen from orbit. "
        + STYLE
    ),
    "us-precedents": (
        "A wide aerial view of Battery Park City and the southern tip of "
        "Manhattan from the Hudson River, golden hour, the rectangular "
        "reclaimed fill clearly legible against the original shoreline. "
        "Monumental but understated. " + STYLE
    ),
    "economics-and-value-capture": (
        "Abstract overhead view of a new coastal district: tidy parcels, canals, "
        "harbor basin, a ring road defining the outer edge of a reclaimed "
        "polder-like development. No text. The geometry evokes value being "
        "produced from water. Clean lines, cool palette with warm window "
        "lights. " + STYLE
    ),
    "risk-and-insurance": (
        "A stylized aerial of a coastal district under partial flooding from a "
        "storm surge: water has breached into street grid at the outer edge, "
        "but the inner district remains dry behind a visible levee line. Stark, "
        "diagrammatic, not catastrophic. Steel gray sky. " + STYLE
    ),
    "institutions-and-permitting": (
        "A formal aerial of a coastal project site marked with survey flags, "
        "boundary buoys, environmental monitoring towers, and a staging area "
        "with a single barge at dock. Waiting for approval. Overcast light, "
        "all edges hard. Evokes process and authorization. " + STYLE
    ),
    "florida-case-study": (
        "High aerial view of the southern Florida peninsula at late afternoon, "
        "with visible reef line, barrier islands, the Miami grid, and a long "
        "sandy curve of coastline. The land is low and flat, the water is "
        "turquoise, the sky is big. Evokes the specific geometry of Florida "
        "coastal exposure. " + STYLE
    ),
    "roadmap-and-ecosystem": (
        "Schematic-industrial aerial of a multi-phase coastal project under "
        "construction with distinct zones visible: one phase already vegetated "
        "and built upon, a middle phase with bare fill and bulldozers, a third "
        "phase still a flooded cell awaiting sand. Sequence of construction "
        "legible as a timeline. " + STYLE
    ),
    "beyond-coastline": (
        "A vast high-altitude aerial at dawn showing terrain that transitions "
        "from coastline to elevated upland to inland watershed: a barrier "
        "island in the foreground, raised urban grade mid-frame, a dammed "
        "reservoir and irrigation canals in the far distance, mountains on the "
        "horizon with snowpack. Composite scale of territorial engineering. "
        + STYLE
    ),
}


def load_client() -> OpenAI:
    if not KEY_PATH.exists():
        sys.exit(f"API key not found at {KEY_PATH}")
    key = KEY_PATH.read_text().strip()
    return OpenAI(api_key=key)


def generate_one(client: OpenAI, slug: str, prompt: str, out_path: Path) -> None:
    print(f"[gen] {slug} -> {out_path.name}")
    result = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size="1536x1024",
        quality="high",
        output_format="png",
        n=1,
    )
    image_bytes = base64.b64decode(result.data[0].b64_json)
    out_path.write_bytes(image_bytes)
    print(f"[ok]  wrote {len(image_bytes) / 1024:.0f} KB")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="Generate only this slug")
    parser.add_argument("--dry-run", action="store_true", help="Print prompts only")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenerate images that already exist",
    )
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    slugs = [args.only] if args.only else list(PROMPTS.keys())
    if args.only and args.only not in PROMPTS:
        sys.exit(f"unknown slug: {args.only}")

    if args.dry_run:
        for slug in slugs:
            print(f"--- {slug} ---")
            print(PROMPTS[slug])
            print()
        return 0

    client = load_client()
    for slug in slugs:
        out_path = OUT_DIR / f"{slug}.png"
        if out_path.exists() and not args.overwrite:
            print(f"[skip] {slug} (exists)")
            continue
        try:
            generate_one(client, slug, PROMPTS[slug], out_path)
        except Exception as exc:
            print(f"[err] {slug}: {exc}")
            time.sleep(5)
            continue
        time.sleep(2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
