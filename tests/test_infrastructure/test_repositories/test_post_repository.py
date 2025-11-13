from src.infrastructure.repositories.post_repository import InMemoryPostRepository


def test_in_memory_post_repository() -> None:
    """Тестирует репозиторий постов в памяти."""
    repository = InMemoryPostRepository()
    posts = repository.get_all()

    assert len(posts) == len(repository.posts)
    assert posts[0].title == 'First Post'
    assert posts[1].title == 'Second Post'
