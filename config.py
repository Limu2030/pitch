
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    DEBUG = os.getenv('DEBUG')
    


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}    