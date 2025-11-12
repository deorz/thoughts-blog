from abc import ABC, abstractmethod

from src.domain.entities.posts import Post


class IPostRepository(ABC):
    """Interface for a post repository."""

    @abstractmethod
    def get_all(self) -> list[Post]:
        """Get all posts."""
        raise NotImplementedError

    @abstractmethod
    def get_one(self, pk: str) -> Post | None:
        """Get one post by pk."""
        raise NotImplementedError
