import typer

from smartapi.commands import (
    make_module,
    make_controller,
    make_service,
    make_model,
    make_schema,
    make_router,
    make_crud,
    make_job,
    database,
    app_run,
)

app = typer.Typer(help="SmartAPI – Opinionated FastAPI CLI")

app.add_typer(make_module.app, name="make:module")
app.add_typer(make_controller.app, name="make:controller")
app.add_typer(make_service.app, name="make:service")
app.add_typer(make_model.app, name="make:model")
app.add_typer(make_schema.app, name="make:schema")
app.add_typer(make_router.app, name="make:router")
app.add_typer(make_crud.app, name="make:crud")
app.add_typer(make_job.app, name="make:job")

app.add_typer(database.app, name="db")
app.add_typer(database.app, name="make")

app.add_typer(app_run.app, name="app")

def main():
    app()

if __name__ == "__main__":
    main()
