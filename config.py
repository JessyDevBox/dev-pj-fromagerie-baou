import os


class Config:
    APP_ENV = os.environ.get("APP_ENV") or "dev"
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "cle-secrete-par-defaut"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_TRANSLATION_DIRECTORIES = "app/translations"
