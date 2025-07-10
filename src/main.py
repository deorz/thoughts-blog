from fastapi import FastAPI

from src.core.config import init_config


def create_app() -> FastAPI:
    """Создаёт и конфигурирует приложение FastAPI."""
    config = init_config()

    return FastAPI(
        title=config.app_name,
        debug=config.debug,
    )
