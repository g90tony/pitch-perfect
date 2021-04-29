import os

class Config:
    # WTF FORMS SECURITY KEY
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    # SQLALCHEMY KEYS
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://caleb:admin@localhost/pitch_perfect'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    # DISPLAY PICTURE UPLOAD DESTINATION
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    
    # MAIL CONFIGURATION
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}