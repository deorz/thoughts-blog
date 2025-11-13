from typing import Annotated

import fastapi

from src.domain.entities.posts import Post
from src.presentantion.api.dependencies import get_list_posts_use_case, get_post_use_case
from src.use_cases.list_posts import GetPostUseCase, ListPostsUseCase

router = fastapi.APIRouter()


@router.get('/posts')
def list_posts(
    list_posts_use_case: Annotated[ListPostsUseCase, fastapi.Depends(get_list_posts_use_case)],
) -> list[Post]:
    """Возвращает список всех постов."""
    return list_posts_use_case.execute()


@router.get('/posts/{pk}')
def get_one_post(
    get_one_post_use_case: Annotated[GetPostUseCase, fastapi.Depends(get_post_use_case)],
    pk: str,
) -> Post | None:
    """Возвращает один пост по первичному ключу."""
    post = get_one_post_use_case.execute(pk=pk)

    if post is None:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND)

    return post
