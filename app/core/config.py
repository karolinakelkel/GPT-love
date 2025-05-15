from os.path import join, dirname

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """
        Project configuration settings.

        These settings are loaded from the .env file in the root directory.
    """

    DEBUG: bool = False
    SECRET_KEY: str
    DATABASE_URL: str
    OPENAI_API_KEY: str

    LOG_DIR: str = join(dirname(dirname(__file__)), 'logs')
    LOG_FILE_NAME: str = 'gpt-love.log'
    MAX_LOG_SIZE: int = 5 * 1024 * 1024
    LOG_BACKUP_COUNT: int = 5
    LOG_LEVEL: str = 'DEBUG' if DEBUG else 'INFO'

    class Config:
        env_file = join(dirname(dirname(dirname(__file__))), '.env')


settings = Settings()
