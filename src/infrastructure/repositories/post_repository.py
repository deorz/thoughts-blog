import datetime

from src.domain.entities.posts import Post
from src.use_cases.interfaces.post_repository import IPostRepository


class InMemoryPostRepository(IPostRepository):
    """In-memory implementation of a post repository."""

    def __init__(self) -> None:
        """Initialize the repository with some dummy data."""
        self.posts: dict[str, Post] = {
            '9e6dd69f-e135-4ab2-b92e-fe8d2807b66b': Post(
                id='9e6dd69f-e135-4ab2-b92e-fe8d2807b66b',
                title='First Post',
                content='This is the first post.',
                author='Author 1',
                created_at=datetime.datetime(2025, 1, 1, 12, 0, 0, tzinfo=datetime.UTC),
            ),
            '963029e8-7e6a-4316-a585-66beccf793c3': Post(
                id='963029e8-7e6a-4316-a585-66beccf793c3',
                title='Second Post',
                content='This is the second post.',
                author='Author 2',
                created_at=datetime.datetime(2025, 1, 1, 12, 0, 0, tzinfo=datetime.UTC),
            ),
        }

    def get_all(self) -> list[Post]:
        """Get all posts from memory."""
        return list(self.posts.values())

    def get_one(self, pk: str) -> Post | None:
        """Get one post from memory by pk."""
        return self.posts.get(pk)
