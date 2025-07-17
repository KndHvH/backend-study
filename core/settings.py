import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    db_path: str = os.getenv("DB_PATH", "sqlite:///./core/database/data.db")
    
settings = Settings()