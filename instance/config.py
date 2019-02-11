"""API Configuration Module."""
class Config():
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False 

APP_CONFIG = dict(
    develop=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)