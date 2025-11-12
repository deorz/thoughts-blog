import pytest


@pytest.fixture(autouse=True)
def mock_config(mocker) -> None:
    mocker.patch.dict('src.core.config.Config.model_config', {'env_file': '.test_env'})
    mocker.patch.dict(
        'os.environ',
        {
            'APP_NAME': 'Test App',
            'DEBUG': 'True',
        },
    )


@pytest.fixture
def default_config(mocker) -> None:
    mocker.patch.dict(
        'os.environ',
        {
            'APP_NAME': 'Test App',
            'DEBUG': 'True',
        },
    )
