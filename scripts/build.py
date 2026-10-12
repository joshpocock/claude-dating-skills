"""Zip each skill into dist/<skill>.zip for upload to Claude.ai, plus dist/claude-dating-skills-all.zip.

Each zip contains the skill folder at its root (<skill>/SKILL.md), which is what Claude.ai expects.
Usage: python scripts/build.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def add_skill(zf: zipfile.ZipFile, skill_dir: pathlib.Path) -> None:
    for f in sorted(skill_dir.rglob("*")):
        if f.is_file():
            zf.write(f, f.relative_to(SKILLS).as_posix())


def main() -> None:
    DIST.mkdir(exist_ok=True)
    skills = sorted(d for d in SKILLS.iterdir() if (d / "SKILL.md").is_file())
    for d in skills:
        with zipfile.ZipFile(DIST / f"{d.name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            add_skill(zf, d)
        print(f"dist/{d.name}.zip")
    with zipfile.ZipFile(DIST / "claude-dating-skills-all.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        for d in skills:
            add_skill(zf, d)
    print("dist/claude-dating-skills-all.zip")


if __name__ == "__main__":
    main()
