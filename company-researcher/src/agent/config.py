import os
from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    # ENVIRONMENT VARIABLES 
    AZURE_OPENAI_API_KEY_4O_MINI:str = os.getenv("AZURE_OPENAI_API_KEY_4O_MINI", "Crypto ChatBot")
    AZURE_OPENAI_ENDPOINT_4O_MINI:str = os.getenv("AZURE_OPENAI_ENDPOINT_4O_MINI", "/api/v1")
    AZURE_ENGINE_4O_MINI:str = os.getenv("AZURE_ENGINE_4O_MINI","../data/")
    AZURE_MODEL_NAME_4O_MINI:str = os.getenv("AZURE_MODEL_NAME_4O_MINI","../logs/")
    AZURE_REGION_4O_MINI:str = os.getenv("AZURE_REGION_4O_MINI")
    AZURE_OPENAI_API_VERSION_4O_MINI:str = os.getenv("AZURE_OPENAI_API_VERSION_4O_MINI")
    TAVILY_API_KEY:str = os.getenv("TAVILY_API_KEY")
    
    class Config:
        case_sensitive = True
    
settings = Settings()