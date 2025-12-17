import typer
from pathlib import Path

from smartapi.utils.naming import to_snake
from smartapi.utils.templates import render

app = typer.Typer()

BASE_MODULES = Path("app/modules")


@app.command("make:crud")
def make_crud(
    module: str,
    entity: str,
    from_model: bool = typer.Option(False, "--from-model"),
    controller: str = typer.Option(None, "--controller"),
    readonly: bool = typer.Option(False, "--readonly"),
    no_delete: bool = typer.Option(False, "--no-delete"),
):
    module_snake = to_snake(module)
    entity_snake = to_snake(entity)

    module_path = BASE_MODULES / module_snake
    module_path.mkdir(parents=True, exist_ok=True)

    model_path = module_path / "model" / f"{entity_snake}_model.py"
    schema_path = module_path / "schemas" / f"{entity_snake}_schema.py"
    service_path = module_path / "service" / f"{entity_snake}_service.py"

    controller_name = controller or entity
    controller_snake = to_snake(controller_name)
    controller_path = module_path / "controller" / f"{controller_snake}_controller.py"

    router_path = module_path / "router.py"

    # model
    if not from_model and not model_path.exists():
        model_path.write_text(render(
            "crud/model.py.tpl",
            entity=entity,
            entity_snake=entity_snake
        ))

    # schema
    schema_path.write_text(render(
        "crud/schema.py.tpl",
        entity=entity
    ))

    # service
    service_path.write_text(render(
        "crud/service.py.tpl",
        entity=entity,
        entity_snake=entity_snake,
        module_snake=module_snake
    ))

    # controller base
    if not controller_path.exists():
        controller_path.write_text(render(
            "crud/controller.base.py.tpl",
            controller_name=controller_name,
            entity=entity,
            entity_snake=entity_snake,
            module_snake=module_snake
        ))

    # controller methods
    with open(controller_path, "a", encoding="utf-8") as f:
        f.write(render(
            "crud/controller.methods.py.tpl",
            entity_snake=entity_snake
        ))

        if not readonly:
            f.write(render(
                "crud/controller.methods.delete.py.tpl",
                entity_snake=entity_snake
            ))

    # router
    with open(router_path, "a", encoding="utf-8") as f:
        f.write(render(
            "crud/router.routes.py.tpl",
            entity=entity,
            entity_snake=entity_snake
        ))

        if not readonly and not no_delete:
            f.write(render(
                "crud/router.routes.delete.py.tpl",
                entity_snake=entity_snake
            ))

    typer.echo(f"✅ CRUD '{entity}' criado no módulo '{module}'")
