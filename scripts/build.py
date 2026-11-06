#!/usr/bin/env python3
"""Build Mr Wolf's public app database and render its declarative A2UI surface."""
from __future__ import annotations
import json
import pathlib
import shutil
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import a2ui_render as AR

SOURCE = ROOT / "leaderboard.json"
TEMPLATE = ROOT / "_ui" / "index.a2ui.json"
OUT = ROOT / "dist"

def fail(message: str) -> None:
    raise SystemExit("Mr Wolf build: " + message)

def main() -> None:
    db = json.loads(SOURCE.read_text(encoding="utf-8"))
    if db.get("schema") != "cedwyn_mr_wolf_leaderboard/v2":
        fail("unsupported leaderboard schema")
    rows = db.get("rows")
    if not isinstance(rows, list) or not rows:
        fail("leaderboard rows are missing")
    seen = set()
    minimum = db.get("minimum_per_limb")
    if not isinstance(minimum, int) or minimum <= 0:
        fail("minimum_per_limb must be a positive integer")
    for row in rows:
        rid = row.get("id")
        if not rid or rid in seen:
            fail("missing or duplicate row id: " + str(rid))
        seen.add(rid)
        limbs = row.get("limbs") or {}
        if set(limbs) != {"a", "b", "c", "d"}:
            fail(rid + ": exactly four proof limbs are required")
        if any(not isinstance(v, int) or v < 0 or v > 50 for v in limbs.values()):
            fail(rid + ": limb score outside 0–50")
        if row.get("score") != sum(limbs.values()):
            fail(rid + ": total does not equal the four limb scores")
        expected = min(100, int(min(limbs.values()) / minimum * 100))
        if row.get("threshold_progress_percent") != expected:
            fail(rid + ": weakest-limb progress does not match backend scores")
        for record in row.get("records", []):
            href = record.get("href", "")
            if not href.startswith("/") or href.startswith("//"):
                fail(rid + ": record link must be site-relative")
    if not isinstance(db.get("route_gate"), dict) or not isinstance(db.get("rubric"), dict):
        fail("route gate and scoring rubric must be present")

    model = {
        "database": db,
        "meta": {
            "app": "mr-wolf",
            "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "source": "leaderboard.json",
            "rows": len(rows),
            "leaderboard_version": db.get("version")
        }
    }
    messages = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    found_surface = found_data = False
    for message in messages:
        if "createSurface" in message:
            found_surface = True
            if message["createSurface"].get("catalogId") != AR.CATALOG_ID:
                fail("A2UI catalog id mismatch")
        if "updateDataModel" in message:
            found_data = True
            message["updateDataModel"]["value"] = model
    if not found_surface or not found_data:
        fail("template must create a surface and provide a data model")

    rendered = AR.render(messages)
    if not rendered.startswith("<!doctype html>") or '<main class="mww">' not in rendered:
        fail("rendered document is missing the main content root")
    if any(x in rendered for x in ("What's the time, Mr Wolf?", "15 leads tested", "Our case, prospective")):
        fail("legacy preamble remains in rendered output")
    if rendered.count("mw-row mw-lead-card") != len(rows):
        fail("A2UI did not render one card per backend row")
    if rendered.count("mw-score-chip") != len(rows) * 4:
        fail("A2UI did not render four limb values for every row")
    if "Procedural route" not in rendered or "Scoring method" not in rendered:
        fail("procedural route or scoring method is missing")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(rendered, encoding="utf-8")
    (OUT / "_db").mkdir(exist_ok=True)
    (OUT / "_db" / "view.json").write_text(json.dumps(model, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (OUT / "_db" / "leaderboard.json").write_text(json.dumps(db, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (OUT / "_ui").mkdir(exist_ok=True)
    (OUT / "_ui" / "index.surface.a2ui.json").write_text(json.dumps(messages, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    shutil.copy2(ROOT / "mw.css", OUT / "mw.css")
    shutil.copy2(ROOT / "lang.json", OUT / "lang.json")
    shutil.copy2(SOURCE, OUT / "leaderboard.json")
    # Keep the checked, generated index at repository root as a static fallback;
    # Pages publishes dist/ when its A2UI build command is configured.
    (ROOT / "index.html").write_text(rendered, encoding="utf-8")
    print("Mr Wolf build OK: %d rows, A2UI v0.9, source leaderboard v%s" % (len(rows), db.get("version")))

if __name__ == "__main__":
    main()
