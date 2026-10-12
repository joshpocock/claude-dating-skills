"""Run each skill against its fictional test input(s) via the Claude Code CLI (`claude -p`).

Usage: python scripts/run_tests.py [skill-name-or-input-stem ...]

Three kinds of test:
- tests/inputs/<skill>[-variant].md      single turn, no tools (like a plain chat).
- tests/inputs/<skill>-web.md            single turn with web search allowed (venue lookups).
- tests/inputs/<skill>-agents.md         single turn with the subagent tool allowed (the reply council's
                                         three advisors run as real parallel Claude Code subagents).
- tests/sessions/<name>/NN-<skill>.md    several turns, each a NEW `claude -p` session in the same
                                         temporary folder with file tools, to check that the
                                         Claude Code log and voice profile persist between sessions.

Outputs are written to tests/outputs/<input-stem>.md and tests/outputs/session-<name>.md
"""
import concurrent.futures as cf
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
INPUTS = ROOT / "tests" / "inputs"
SESSIONS = ROOT / "tests" / "sessions"
OUTPUTS = ROOT / "tests" / "outputs"


def skill_for(stem: str) -> pathlib.Path:
    names = sorted((d.name for d in (ROOT / "skills").iterdir()), key=len, reverse=True)
    for name in names:
        if stem == name or stem.startswith(name + "-"):
            return ROOT / "skills" / name / "SKILL.md"
    raise SystemExit(f"no skill for {stem}")


def claude(prompt: str, tools: str, cwd: pathlib.Path | None = None) -> str:
    cmd = ["claude", "-p", "--tools", tools]
    if tools:
        cmd += ["--allowedTools", tools, "--permission-mode", "acceptEdits"]
    res = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
        shell=sys.platform == "win32", cwd=cwd,
    )
    return res.stdout.strip() or res.stderr.strip()


def claude_agents(prompt: str) -> str:
    """Run with the subagent tool and read the event stream, so the test records how many subagents
    really launched and whether they were launched together (same assistant message = parallel)."""
    cmd = ["claude", "-p", "--tools", "Agent", "--allowedTools", "Agent", "--permission-mode", "acceptEdits",
           "--output-format", "stream-json", "--verbose"]
    res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
                         shell=sys.platform == "win32")
    launches, final = [], ""
    for line in res.stdout.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "assistant" and not ev.get("parent_tool_use_id"):
            calls = [c for c in ev["message"].get("content", []) if c.get("type") == "tool_use" and c.get("name") in ("Agent", "Task")]
            if calls:
                launches.append((ev["message"].get("id"), len(calls)))
        elif ev.get("type") == "result":
            final = ev.get("result", "")
    total = sum(n for _, n in launches)
    batches = len({mid for mid, _ in launches})
    note = "\n\n---\n" + f"Tool log: {total} subagent(s) launched in {batches} assistant message(s)" + (" (parallel)." if total and batches == 1 else ".")
    return (final.strip() or res.stderr.strip()) + note


def wrap(skill_text: str, message: str, tool_note: str) -> str:
    return (
        "You have the following skill loaded. Follow its instructions exactly when answering "
        "the user's message. This is a single-turn test: if the skill says to ask questions "
        f"first and the user already supplied the answers, proceed. {tool_note}\n\n"
        f"<skill>\n{skill_text}\n</skill>\n\n<user_message>\n{message}\n</user_message>"
    )


def run(inp: pathlib.Path) -> str:
    skill = skill_for(inp.stem).read_text(encoding="utf-8")
    msg = inp.read_text(encoding="utf-8")
    if inp.stem.endswith("-web"):
        out = claude(wrap(skill, msg, "You may use web search. Do not use any other tools."), "WebSearch")
    elif inp.stem.endswith("-agents"):
        out = claude_agents(wrap(skill, msg, "You are in Claude Code. You may use the Agent tool to launch subagents. "
                                 "Do not use any other tools."))
    else:
        out = claude(wrap(skill, msg, "Do not use any tools."), "")
    (OUTPUTS / f"{inp.stem}.md").write_text(
        f"# Test: {inp.stem}\n\n## Input (fictional)\n\n{msg}\n\n## Output\n\n{out}\n", encoding="utf-8",
    )
    return f"{inp.stem}: {len(out)} chars"


def run_session(folder: pathlib.Path) -> str:
    work = pathlib.Path(tempfile.mkdtemp(prefix="dating-session-"))
    parts = [f"# Session test: {folder.name}\n\nEach turn is a separate `claude -p` session (no shared chat history) "
             "running in the same empty folder with file tools (Read, Write, Edit, Glob). Anything a later turn "
             "knows must have come from the files earlier turns saved.\n"]
    try:
        for turn in sorted(folder.glob("*.md")):
            skill_stem = turn.stem.split("-", 1)[1]
            skill = skill_for(skill_stem).read_text(encoding="utf-8")
            msg = turn.read_text(encoding="utf-8")
            note = ("You are running in Claude Code in the user's project folder (the current working directory). "
                    "You may use the Read, Write, Edit and Glob tools there.")
            out = claude(wrap(skill, msg, note), "Read,Write,Edit,Glob", cwd=work)
            parts.append(f"\n## Turn {turn.stem}\n\n### User (fictional)\n\n{msg}\n\n### Claude\n\n{out}\n")
        parts.append("\n## Files on disk after the last turn\n")
        for f in sorted(work.rglob("*")):
            if f.is_file():
                rel = f.relative_to(work).as_posix()
                parts.append(f"\n### {rel}\n\n```markdown\n{f.read_text(encoding='utf-8', errors='replace').strip()}\n```\n")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    (OUTPUTS / f"session-{folder.name}.md").write_text("".join(parts), encoding="utf-8")
    return f"session-{folder.name}: done"


if __name__ == "__main__":
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    wanted = sys.argv[1:]
    files = [p for p in sorted(INPUTS.glob("*.md")) if not wanted or any(p.stem.startswith(w) for w in wanted)]
    sessions = [d for d in sorted(SESSIONS.iterdir()) if d.is_dir()] if SESSIONS.exists() else []
    sessions = [d for d in sessions if not wanted or any(("session-" + d.name).startswith(w) or w == "session" for w in wanted)]
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        jobs = [ex.submit(run, f) for f in files] + [ex.submit(run_session, d) for d in sessions]
        for j in cf.as_completed(jobs):
            print(j.result())
