from pydantic import BaseSettings, Field

class EnvConfig(BaseSettings):
    db_uri = Field(default="db_uri", env="DB_URI")
