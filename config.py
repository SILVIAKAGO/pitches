import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kago@localhost/pitch'
    SECRET_KEY = 'kago'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgres://sdvhkdqqkgedlj:1e6e0541b42816b697dc2e3252486f9dbfbc3b69c07f498bd97d836ec81bc5ca@ec2-34-202-65-210.compute-1.amazonaws.com:5432/d61i2figga0fqf'
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
 