import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get("DEV_DATABASE_URL")
            or "driver://주소"
    )

class ProductionConfig(Config):
    DEBUG = False
    NAME = "PROD"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get("DEV_DATABASE_URL")
            or "driver://주소")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    NAME = "DEV"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get("DEV_DATABASE_URL")
            or "driver://주소")


class LocalingConfig(Config):
    LOCAL = True
    NAME = "LOCAL"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get("DEV_DATABASE_URL")
            or "postgresql://postgres:postgres@localhost:5432/service") #jdbc:postgresql://localhost:5432/service


config = {"local": LocalingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}