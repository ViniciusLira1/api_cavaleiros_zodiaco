from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR = "/api/v1"
    DB_URL = "mysql+asyncmy://root@127.0.0.1:3306/cavaleiros"
    #DB_URL = "mysql+asyncmy://root:senai@127.0.0.1:3306/cavaleiros"
    DBBaseModel = declarative_base()
    
class Config:
    case_sensitive = False
    env_file = ".venv"
settings = Settings()