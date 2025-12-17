import typer
from pathlib import Path

from smartapi.utils.naming import to_snake
from smartapi.utils.templates import render

app = typer.Typer()

BASE_MODULES = Path("app/modules")


@app.command("make:module")
def make_module(module: str):
    """
    Cria um módulo com:
    - camadas padrão
    - controller base
    - router base
    """

    module_snake = to_snake(module)
    module_path = BASE_MODULES / module_snake

    module_path.mkdir(parents=True, exist_ok=True)
    (module_path / "__init__.py").touch(exist_ok=True)

    for layer in ["controller", "service", "model", "schemas"]:
        layer_path = module_path / layer
        layer_path.mkdir(exist_ok=True)
        (layer_path / "__init__.py").touch(exist_ok=True)

    controller_file = module_path / "controller" / f"{module_snake}_controller.py"
    if not controller_file.exists():
        controller_file.write_text(
            render(
                "module/controller.py.tpl",
                module=module
            )
        )

    router_file = module_path / "router.py"
    if not router_file.exists():
        router_file.write_text(
            render(
                "module/router.py.tpl",
                module=module,
                module_snake=module_snake
            )
        )

    typer.echo(f"✅ Módulo '{module}' criado com sucesso")
