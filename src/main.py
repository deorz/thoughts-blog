from fastapi import FastAPI

from src.core.initializer import init_config, init_di_container


def create_app() -> FastAPI:
    """Создаёт и конфигурирует приложение FastAPI."""
    config = init_config()

    app = FastAPI(
        title=config.app_name,
        debug=config.debug,
    )

    init_di_container(app=app, config=config)

    return app
