
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Python Demo Project"
    API_V1_STR: str = "/api/v1"
    
    # 数据库配置
    # 默认使用 SQLite，但在生产环境中可以覆盖为 PostgreSQL/MySQL
    # 类似于 DATABASE_URL 环境变量
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"

    # Pydantic V2 配置
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()
