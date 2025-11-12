import fastapi
import fastapi.testclient
import pytest
import syrupy

from src.main import create_app


@pytest.fixture
def client() -> fastapi.testclient.TestClient:
    return fastapi.testclient.TestClient(create_app())


def test_list_posts(
    client: fastapi.testclient.TestClient, snapshot: syrupy.assertion.SnapshotAssertion,
) -> None:
    """Test listing all posts."""
    response = client.get('/posts')
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == snapshot


def test_get_one_post_success(
    client: fastapi.testclient.TestClient, snapshot: syrupy.assertion.SnapshotAssertion,
) -> None:
    """Test getting one post successfully."""
    response = client.get('/posts/9e6dd69f-e135-4ab2-b92e-fe8d2807b66b')
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == snapshot


def test_get_one_post_not_found(client: fastapi.testclient.TestClient) -> None:
    """Test getting one post that does not exist."""
    response = client.get('/posts/non-existing-id')
    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
