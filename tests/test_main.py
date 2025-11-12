import fastapi
import pytest

from src.main import create_app


class TestCreateApp:
    @pytest.mark.usefixtures('default_config')
    def test_create_app(self) -> None:
        app = create_app()

        assert isinstance(app, fastapi.FastAPI)
        assert app.title == 'Test App'
        assert app.debug is True

    @pytest.mark.usefixtures('default_config')
    def test_route_list(self) -> None:
        app = create_app()

        routes = sorted([(route.path, sorted(route.methods)) for route in app.routes])

        assert routes == sorted([
            ('/posts', ['GET']),
            ('/openapi.json', ['GET', 'HEAD']),
            ('/docs', ['GET', 'HEAD']),
            ('/docs/oauth2-redirect', ['GET', 'HEAD']),
            ('/redoc', ['GET', 'HEAD']),
        ])
