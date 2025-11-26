import pathlib

import pydantic
import pytest

from src.core.initializer import init_config


class TestInitConfig:
    @pytest.fixture
    def temp_env(self, mocker):
        env_file = pathlib.Path('.env.test')
        env_content = """APP_NAME=Test App From Env
DEBUG=False
DB_PATH=blog_from_env.sqlite3"""

        env_file.write_text(
            env_content,
            encoding='utf-8',
        )

        mocker.patch.dict('src.core.config.Config.model_config', {'env_file': env_file})
        mocker.patch.dict('os.environ', {}, clear=True)

        yield env_file

        env_file.unlink()

    def test_init_successful(self) -> None:
        config = init_config()

        assert config.app_name == 'Test App'
        assert config.debug is True
        assert config.db_path == 'blog.sqlite3'

    @pytest.mark.usefixtures('temp_env')
    def test_init_from_env_file(self) -> None:
        config = init_config()

        assert config.app_name == 'Test App From Env'
        assert config.debug is False
        assert config.db_path == 'blog_from_env.sqlite3'

    def test_init_error(self, mocker) -> None:
        mocker.patch.dict('os.environ', {}, clear=True)
        with pytest.raises(pydantic.ValidationError):
            init_config()
