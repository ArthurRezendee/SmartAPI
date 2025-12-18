from __future__ import annotations

from pathlib import Path
from string import Template


def render_template(
    *,
    template: str,
    target: Path,
    context: dict,
):
    """
    Renderiza um template .tpl substituindo variáveis
    e grava no caminho target
    """

    templates_base = Path(__file__).resolve().parent.parent / "templates"
    template_path = templates_base / template

    if not template_path.exists():
        raise FileNotFoundError(f"Template não encontrado: {template_path}")

    content = template_path.read_text(encoding="utf-8")

    rendered = Template(content).safe_substitute(context)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rendered, encoding="utf-8")
