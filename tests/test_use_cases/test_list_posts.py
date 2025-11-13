"""Тесты для use case получения списка постов."""

import pytest_mock

from src.domain.entities.posts import Post
from src.use_cases.list_posts import ListPostsUseCase


def test_list_posts_use_case(mocker: pytest_mock.MockerFixture) -> None:
    """Тестирует use case получения списка постов."""
    mock_post_repository = mocker.Mock()
    mock_post_repository.get_all.return_value = [
        Post(id='1', title='Test Post', content='Test Content', author='Test Author'),
    ]

    list_posts_use_case = ListPostsUseCase(post_repository=mock_post_repository)
    posts = list_posts_use_case.execute()

    assert len(posts) == 1
    assert posts[0].title == 'Test Post'
    mock_post_repository.get_all.assert_called_once()
