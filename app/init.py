from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import settings


def create_app():
    app = FastAPI(title="Bibioteca API", docs_url="/")

    register_tortoise(
        app,
        db_url=f"postgres://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:5432/{settings.DB_NAME}",
        modules={"models": ["app.biblioteca.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    from app.biblioteca.endpoints import autor_endpoint, livro_endpoint

    app.include_router(autor_endpoint, prefix="/autor", tags=["autor"])
    app.include_router(livro_endpoint, prefix="/livro", tags=["livro"])

    return app