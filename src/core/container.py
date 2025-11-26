import aiosqlite
from dishka import Provider, Scope, provide

from src.core.config import Config


class SqliteConnectionProvider(Provider):
    """Поставщик подключения к базе данных SQLite."""

    def __init__(self, config: Config) -> None:
        super().__init__()
        self.__config = config

    @provide(scope=Scope.APP)
    async def get_connection(self) -> aiosqlite.Connection:
        """Получает подключение к базе данных SQLite."""
        return await aiosqlite.connect(database=self.__config.db_path)
