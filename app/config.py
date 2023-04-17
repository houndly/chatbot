"""
	Module to handle environments configurations
"""

from app.common.constants import CredentialsFiles


class Config(object):
    DEBUG = False
    TESTING = False
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')

# class ProductionConfig(Config):
#     DATABASE_URI = os.environ.get('DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True

class QaConfig(Config):
    TESTING = True

config = {
    # 'production': ProductionConfig,
    'development': DevelopmentConfig,
    'qa': QaConfig,
    'default': DevelopmentConfig
}
