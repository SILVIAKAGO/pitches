import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    print(SQLALCHEMY_DATABASE_URI, 'maratah')
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST ='app/static/photos'

     # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class ProdConfig(Config):
    DEBUG = False
    '''
    Production configurations child class
    '''

class DevConfig(Config):
    '''
    Development configurations child class
    '''

    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig
}