"""Run each skill against its fictional test input(s) via the Claude Code CLI (`claude -p`).

Usage: python scripts/run_tests.py [skill-name-or-input-stem ...]
Outputs are written to tests/outputs/<input-stem>.md
"""
import concurrent.futures as cf
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INPUTS = ROOT / "tests" / "inputs"
OUTPUTS = ROOT / "tests" / "outputs"


def skill_for(stem: str) -> pathlib.Path:
    for d in (ROOT / "skills").iterdir():
        if stem == d.name or stem.startswith(d.name + "-"):
            return d / "SKILL.md"
    raise SystemExit(f"no skill for {stem}")


def run(inp: pathlib.Path) -> str:
    skill = skill_for(inp.stem).read_text(encoding="utf-8")
    prompt = (
        "You have the following skill loaded. Follow its instructions exactly when answering "
        "the user's message. This is a single-turn test: if the skill says to ask questions "
        "first and the user already supplied the answers, proceed. Do not use any tools.\n\n"
        f"<skill>\n{skill}\n</skill>\n\n<user_message>\n{inp.read_text(encoding='utf-8')}\n</user_message>"
    )
    res = subprocess.run(
        ["claude", "-p", "--tools", ""],
        input=prompt, capture_output=True, text=True, encoding="utf-8", shell=sys.platform == "win32",
    )
    out = res.stdout.strip() or res.stderr.strip()
    (OUTPUTS / f"{inp.stem}.md").write_text(
        f"# Test: {inp.stem}\n\n## Input (fictional)\n\n{inp.read_text(encoding='utf-8')}\n\n## Output\n\n{out}\n",
        encoding="utf-8",
    )
    return f"{inp.stem}: {len(out)} chars"


if __name__ == "__main__":
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    wanted = sys.argv[1:]
    files = [p for p in sorted(INPUTS.glob("*.md")) if not wanted or any(p.stem.startswith(w) for w in wanted)]
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for line in ex.map(run, files):
            print(line)
