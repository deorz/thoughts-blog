from fastapi import FastAPI

from src.core.config import init_config
from src.presentantion.api import posts


def create_app() -> FastAPI:
    """Создаёт и конфигурирует приложение FastAPI."""
    config = init_config()

    app = FastAPI(
        title=config.app_name,
        debug=config.debug,
    )

    app.include_router(posts.router)

    return app
