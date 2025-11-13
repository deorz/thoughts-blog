from src.infrastructure.repositories.post_repository import InMemoryPostRepository
from src.use_cases.list_posts import GetPostUseCase, ListPostsUseCase


def get_list_posts_use_case() -> ListPostsUseCase:
    """Возвращает use case для получения списка постов."""
    return ListPostsUseCase(post_repository=InMemoryPostRepository())


def get_post_use_case() -> GetPostUseCase:
    """Возвращает use case для получения поста."""
    return GetPostUseCase(post_repository=InMemoryPostRepository())
