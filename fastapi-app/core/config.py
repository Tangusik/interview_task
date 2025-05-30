from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

class RunCongig(BaseModel):
    host:str = '0.0.0.0'
    port:str = 8000

class ApiPrefix(BaseModel):
    prefix: str = '/api'

class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    max_overflow: int = 50
    pool_size: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

class CorsData(BaseModel):
    allowed_origins: list[str] = ['*']

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False, 
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",)
    run: RunCongig = RunCongig()
    api: ApiPrefix = ApiPrefix()
    db: DBConfig
    cors_data: CorsData = CorsData()



settings = Settings()