"""Zip each skill into dist/<skill>.zip for upload to Claude.ai, plus dist/claude-dating-skills-all.zip.

Each zip contains the skill folder at its root (<skill>/SKILL.md), which is what Claude.ai expects.
Files in shared/ are canonical copies used by more than one skill. Claude.ai takes one skill per zip,
so each user skill gets its own copy: SHARED maps each shared file to the skills that need it, and the
build writes it into <skill>/references/ first (the copies are committed so git-clone installs work too).
Usage: python scripts/build.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
SHARED = {"texting-framework.md": ["dating-opener", "dating-reply-reader"]}


def sync_shared() -> None:
    for name, users in SHARED.items():
        text = (ROOT / "shared" / name).read_bytes()
        for skill in users:
            dest = SKILLS / skill / "references" / name
            dest.parent.mkdir(exist_ok=True)
            if not dest.exists() or dest.read_bytes() != text:
                dest.write_bytes(text)
                print(f"synced shared/{name} -> skills/{skill}/references/")


def add_skill(zf: zipfile.ZipFile, skill_dir: pathlib.Path) -> None:
    for f in sorted(skill_dir.rglob("*")):
        if f.is_file():
            zf.write(f, f.relative_to(SKILLS).as_posix())


def main() -> None:
    sync_shared()
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
