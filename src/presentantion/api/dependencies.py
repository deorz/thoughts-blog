from src.infrastructure.repositories.post_repository import InMemoryPostRepository
from src.use_cases.list_posts import GetPostUseCase, ListPostsUseCase


def get_list_posts_use_case() -> ListPostsUseCase:
    """Get the list posts use case."""
    return ListPostsUseCase(post_repository=InMemoryPostRepository())


def get_post_use_case() -> GetPostUseCase:
    """Get the list posts use case."""
    return GetPostUseCase(post_repository=InMemoryPostRepository())
