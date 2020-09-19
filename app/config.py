import os
from app import basedir


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/Konop'
    SECRET_KEY = 'dev_secret_key_test_)(@$(*JF#'


app_config = {
    'dev': DevelopmentConfig,
}