import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lilly:1234@localhost/clouds'
    

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql://ynzxcynqwkzwgu:d24546c110c7ca60e310f6bc1ae1d4cba7ea2b151cdb96dce4a6aa5b0cdd70f9@ec2-44-194-117-205.compute-1.amazonaws.com:5432/d45d0c3aat5480'
                            
    SQLALCHEMY_DATABASE_URI='postgresql://wgpxvhudzrcosd:1e93513e7238b0dc344a40fef2ca70073c27b0e480749df88511ad9096a57a6c@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d93lur41ej8f2s'

class DevConfig(Config):
    DEBUG = True
    
    

config_options = {
'development':DevConfig,
'production':ProdConfig
} 