from src.domain.entities.posts import Post
from src.use_cases.interfaces.post_repository import IPostRepository


class ListPostsUseCase:
    """Use case для получения списка всех постов."""

    def __init__(self, post_repository: IPostRepository):
        """Инициализирует use case."""
        self.post_repository = post_repository

    def execute(self) -> list[Post]:
        """Выполняет use case."""
        return self.post_repository.get_all()


class GetPostUseCase:
    """Use case для получения одного поста."""

    def __init__(self, post_repository: IPostRepository):
        """Инициализирует use case."""
        self.post_repository = post_repository

    def execute(self, pk: str) -> Post | None:
        """Выполняет use case."""
        return self.post_repository.get_one(pk=pk)
