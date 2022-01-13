import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    LOGIN_VIEW = 'auth.login'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}