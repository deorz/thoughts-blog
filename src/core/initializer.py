import fastapi
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from src.core.config import Config
from src.core.container import SqliteConnectionProvider


def init_config() -> Config:
    """Инициализирует конфигурацию приложения."""
    return Config()


def init_di_container(app: fastapi.FastAPI, config: Config) -> None:
    """Создание контейнера с зависимостями."""
    di_container = make_async_container(SqliteConnectionProvider(config=config))
    setup_dishka(container=di_container, app=app)
