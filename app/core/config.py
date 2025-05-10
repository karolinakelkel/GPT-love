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

    class Config:
        env_file = join(dirname(dirname(dirname(__file__))), ".env")
