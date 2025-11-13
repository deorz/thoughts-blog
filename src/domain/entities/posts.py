import datetime
from typing import Annotated

import pydantic


class Post(pydantic.BaseModel):
    """Представляет пост блога."""

    id: Annotated[str, pydantic.Field(description='Уникальный идентификатор поста.')]
    title: Annotated[str, pydantic.Field(description='Заголовок поста.')]
    content: Annotated[str, pydantic.Field(description='Содержимое поста.')]
    author: Annotated[str, pydantic.Field(description='Автор поста.')]
    created_at: datetime.datetime = pydantic.Field(
        default_factory=datetime.datetime.now,
        description='Временная метка создания поста.',
    )
