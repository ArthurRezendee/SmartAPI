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
    app_run,
    db_migrate,
    db_rollback,
    init
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

app.add_typer(db_migrate.app, name="db:migrate")
app.add_typer(db_rollback.app, name="db:rollback")

app.add_typer(app_run.app, name="app")
app.command("init")(init.init_project)

def main():
    app()

if __name__ == "__main__":
    main()
