import pytest


@pytest.fixture(autouse=True)
def default_config(mocker) -> None:
    mocker.patch.dict('src.core.config.Config.model_config', {'env_file': None})
    mocker.patch.dict(
        'os.environ',
        {
            'APP_NAME': 'Test App',
            'DEBUG': 'True',
            'DB_PATH': 'blog.sqlite3',
        },
    )


@pytest.fixture
def patch_config(mocker):
    def _patch(env_vars: dict[str, str]) -> None:
        mocker.patch.dict('os.environ', env_vars)

    return _patch
