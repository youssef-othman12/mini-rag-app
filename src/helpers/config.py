from ptdantic_settings import BaseSettings , SettingsConfigDict

class settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    class config:
        env_file=".env"
def get_settings():
    return settings()