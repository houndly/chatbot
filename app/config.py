"""
	Module to handle environments configurations
"""

from app.common.constants import GOOGLE_SHEETS


class Config(object):
    DEBUG = False
    TESTING = False
    GOOGLE_SHEETS_CREDS_FILE = GOOGLE_SHEETS


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
