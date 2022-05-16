import os



class Config:
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://fmeutmnsdzdqww:567b5f96281c8fca3b55dd1e364e7df6953150b2eaccbfa3ea9157e4fe9bb793@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d602ucgp8u0q7h'
    

    


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lilly:1234@localhost/pitchhh'
    

config_options = {
'development':DevConfig,
'production':ProdConfig
} 