# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = os.environ.get('APPLICATION_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    dburl = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = '%s?application_name=application' % dburl
    

class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    DEBUG = True
