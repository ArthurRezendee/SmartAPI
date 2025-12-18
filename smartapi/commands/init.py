from __future__ import annotations

from pathlib import Path
import typer

from smartapi.utils.templates import render_template

app = typer.Typer()


def init_project():
    """
    Inicializa um projeto SmartAPI na pasta atual
    """

    root = Path.cwd()

    # --------------------
    # Proteções
    # --------------------
    if (root / "app").exists():
        typer.echo("❌ Projeto já inicializado (pasta 'app' existe).")
        raise typer.Exit(1)

    if (root / "pyproject.toml").exists():
        typer.echo("❌ Já existe um pyproject.toml neste diretório.")
        raise typer.Exit(1)

    typer.echo("🚀 Inicializando projeto SmartAPI...")

    # --------------------
    # Estrutura base
    # --------------------
    (root / "app/core").mkdir(parents=True)
    (root / "app/modules").mkdir(parents=True)
    (root / "app/jobs").mkdir(parents=True)
    (root / "app/shared").mkdir(parents=True)
    (root / "migrations/versions").mkdir(parents=True)
    (root / "docker").mkdir(parents=True)

    # --------------------
    # __init__.py
    # --------------------
    for p in [
        "app",
        "app/core",
        "app/modules",
        "app/jobs",
        "app/shared",
    ]:
        (root / p / "__init__.py").touch()

    # --------------------
    # Templates principais
    # --------------------
    render_template("init/main.py.tpl", root / "app/main.py", {})
    render_template("init/config.py.tpl", root / "app/core/config.py", {})
    render_template("init/database.py.tpl", root / "app/core/database.py", {})
    render_template("init/security.py.tpl", root / "app/core/security.py", {})
    render_template("init/celery_app.py.tpl", root / "app/core/celery_app.py", {})
    render_template("init/controller.py.tpl", root / "app/shared/controller.py", {})

    render_template("init/docker-compose.yml.tpl", root / "docker-compose.yml", {})
    render_template("init/api.Dockerfile.tpl", root / "docker/api.Dockerfile", {})
    render_template("init/worker.Dockerfile.tpl", root / "docker/worker.Dockerfile", {})

    render_template("init/.env.tpl", root / ".env", {})
    render_template("init/.env.example.tpl", root / ".env.example", {})
    render_template("init/gitignore.tpl", root / ".gitignore", {})
    render_template("init/alembic.ini.tpl", root / "alembic.ini", {})
    render_template("init/README.md.tpl", root / "README.md", {})

    typer.echo("✅ Projeto SmartAPI inicializado com sucesso!")
    typer.echo("")
    typer.echo("👉 Próximos passos:")
    typer.echo("   docker compose up")
    typer.echo("   smartapi make:module User")
