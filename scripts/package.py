"""Build the public download from an explicit set of kit paths. No dependencies."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
KIT_FILES = (
    "README.md", "START-HERE.md", "START-PROMPT.txt", "OPEN-FIRST.html",
    "AGENTS.md", "CLAUDE.md", "LICENSE", ".gitignore",
    "assets/banner.svg", "audit/WORKSHOP.md",
    "reference/WORKSPACE.md", "reference/WORKFLOWS.md",
    "reference/CLAUDE-AND-CODEX.md", "reference/SCHEDULING.md",
    "templates/AUDIT-RESULT.md", "templates/AGENTS.md", "templates/CLAUDE.md",
    "templates/CONTEXT-MAP.md", "templates/HANDOVER.md",
    "skills/work-brief/SKILL.md", "skills/review-output/SKILL.md",
    "skills/resume-work/SKILL.md", "routine-example/ROUTINE.md",
    "routine-example/GUARDRAILS.md", "routine-example/maps/sources.md",
    "routine-example/skills/review-work/SKILL.md",
    "routine-example/learnings.md", "routine-example/runs/index.md",
)


def build():
    files = [ROOT / name for name in KIT_FILES]
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected an ordinary kit file: {path.relative_to(ROOT)}")
    target = ROOT / "dist" / "Valentis-AI-Workspace-Audit.zip"
    target.parent.mkdir(exist_ok=True)
    with ZipFile(target, "w", ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, "Valentis-AI-Workspace-Audit/" + path.relative_to(ROOT).as_posix())
    with ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError("Archive failed its integrity check")
    print(f"Built {target.name}: {len(files)} files, {target.stat().st_size:,} bytes")


if __name__ == "__main__":
    build()
