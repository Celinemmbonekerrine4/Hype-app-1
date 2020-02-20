import os
class Config:
    '''
    Describe the general configuarations
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://habbiba:zully1234@localhost/hype"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
     
    # Simple Mde Configs
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # Sending Emails
    # MAIL_SERVER=os.environ.get('MAIL_SERVER')
    # MAIL_PORT=os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    # MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    # UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://habbiba:zully1234@localhost/hype"
    DEBUG = False

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://habbiba:zully1234@localhost/hype"
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}