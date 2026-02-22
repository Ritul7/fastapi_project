from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class AppConfig(BaseSettings):

    app_name:str = "FASTAPI_PROJECT"                            # as it is name dene h, jo env file me diye h, uppercase- lowercase wo sab handle krlega pydantic(Basesetitngs)
    app_env:str = "development"
    database_url:str

    model_config = SettingsConfigDict(env_file=".env")          #This line tells pydantic to read env variables form the .env file


@lru_cache
def getAppConfig():
    return AppConfig()              # everytime it is called, it reads .env file, so intead of reading evrytime, lru_cache helps in giving the stored result



# BaseSettings -> Tells pydantic to automatically read env variables and .env file into python class and allows centralized configuration management
# functools... lru cache -> Caches the result of a function so it is not recreated agian n again