from fastapi import FastAPI

from src.core.initializer import init_config, init_di_container
from src.presentantion.api import posts


def create_app() -> FastAPI:
    """Создаёт и конфигурирует приложение FastAPI."""
    config = init_config()

    app = FastAPI(
        title=config.app_name,
        debug=config.debug,
    )

    init_di_container(app=app, config=config)

    app.include_router(posts.router)

    return app
