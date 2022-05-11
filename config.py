
import os

from flask_sqlalchemy import SQLAlchemy



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