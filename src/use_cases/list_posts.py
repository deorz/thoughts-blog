from src.domain.entities.posts import Post
from src.use_cases.interfaces.post_repository import IPostRepository


class ListPostsUseCase:
    """Use case for listing all posts."""

    def __init__(self, post_repository: IPostRepository):
        """Initialize the use case."""
        self.post_repository = post_repository

    def execute(self) -> list[Post]:
        """Execute the use case."""
        return self.post_repository.get_all()


class GetPostUseCase:
    """Use case for getting one post."""

    def __init__(self, post_repository: IPostRepository):
        """Initialize the use case."""
        self.post_repository = post_repository

    def execute(self, pk: str) -> Post | None:
        """Execute the use case."""
        return self.post_repository.get_one(pk=pk)
