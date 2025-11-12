import datetime
from typing import Annotated

import pydantic


class Post(pydantic.BaseModel):
    """Represents a blog post."""

    id: Annotated[str, pydantic.Field(description='The unique identifier of the post.')]
    title: Annotated[str, pydantic.Field(description='The title of the post.')]
    content: Annotated[str, pydantic.Field(description='The content of the post.')]
    author: Annotated[str, pydantic.Field(description='The author of the post.')]
    created_at: datetime.datetime = pydantic.Field(
        default_factory=datetime.datetime.now,
        description='The timestamp when the post was created.',
    )
