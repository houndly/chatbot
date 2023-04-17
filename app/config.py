"""
	Module to handle environments configurations
"""

from app.common.constants import GOOGLE_SHEETS


class Config(object):
    DEBUG = False
    TESTING = False
    GOOGLE_SHEETS_CREDS_FILE = 	GOOGLE_SHEETS
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
