from base import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from contextlib import asynccontextmanager
from uvicorn.config import Config
from uvicorn.server import Server
from api.routers.settings import router as settings_router
import threading
import tomllib


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def get_version_from_pyproject(path="pyproject.toml") -> str:
    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
            return data["tool"]["poetry"]["version"]
    except Exception:
        return "0.0.0"


def create_app() -> FastAPI:
    app = FastAPI(
        title="Plex Debrid",
        description="Local API to control and configure plex_debrid settings",
        version=get_version_from_pyproject(),
        redoc_url=None,
        lifespan=lifespan,
    )

    app.include_router(settings_router, prefix="/settings", tags=["Settings"])

    for route in app.routes:
        if isinstance(route, APIRoute):
            logger.debug(f"Route: {route.path} | Methods: {route.methods}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


def start_fastapi_process(host: str = "0.0.0.0", port: int = 8000, log_level: str = "info"):
    app = create_app()

    def run_server():
        config = Config(
            app=app,
            host=host,
            port=port,
            log_config=None,
            log_level=log_level,
        )
        server = Server(config)
        server.run()

    uvicorn_thread = threading.Thread(target=run_server, daemon=True)
    uvicorn_thread.start()

    logger.info(f"Started Plex Debrid API at http://{host}:{port}")
