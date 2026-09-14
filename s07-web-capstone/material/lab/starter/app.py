"""Punto de partida: salud del servidor. La práctica implementa el resto."""
from pathlib import Path
from fastapi import FastAPI


def create_app(data_dir: Path) -> FastAPI:
    app = FastAPI(title="Starter S07")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


def local_app() -> FastAPI:
    return create_app(Path(".data"))
