import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    """Конфигурация приложения."""

    app_name: str
    debug: bool
    db_path: str

    model_config = pydantic_settings.SettingsConfigDict(
        case_sensitive=True,
        env_file='.env',
        alias_generator=lambda x: x.upper(),
    )
