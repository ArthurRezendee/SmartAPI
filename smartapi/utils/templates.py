from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "templates"

def render(template: str, **context) -> str:
    path = TEMPLATES_DIR / template
    content = path.read_text(encoding="utf-8")
    return content.format(**context)
