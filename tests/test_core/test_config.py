import pydantic
import pytest

from src.core.config import init_config


class TestInitConfig:
    @pytest.mark.usefixtures('default_config')
    def test_init_successful(self) -> None:
        config = init_config()

        assert config.app_name == 'Test App'
        assert config.debug is True

    def test_init_error(self) -> None:
        with pytest.raises(pydantic.ValidationError):
            init_config()
