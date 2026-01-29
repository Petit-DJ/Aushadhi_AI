from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_env: str = "development"
    database_url: str = ""
    chembl_api_url: str = "https://www.ebi.ac.uk/chembl/api/data"
    allowed_origins: str = "http://localhost:3000"
    
    class Config:
        env_file = ".env"

settings = Settings()
