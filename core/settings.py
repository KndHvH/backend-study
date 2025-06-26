import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    
settings = Settings()