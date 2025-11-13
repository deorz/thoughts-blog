from abc import ABC, abstractmethod

from src.domain.entities.posts import Post


class IPostRepository(ABC):
    """Интерфейс репозитория постов."""

    @abstractmethod
    async def get_all(self) -> list[Post]:
        """Возвращает все посты."""
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, pk: str) -> Post | None:
        """Возвращает один пост по первичному ключу."""
        raise NotImplementedError
