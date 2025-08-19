
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = "dev"
    db_path: str = "sqlite:///./core/database/data.db"
    
    class Config:
            env_file = ".env"

settings = Settings()