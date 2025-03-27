from flask import Flask, request, session, g
from flask_babel import Babel
from config import Config

babel = Babel()


def get_locale():
    # 1. Check if language is store in session
    if "language" in session:
        return session["language"]

    # 2. Try to detect prefered navigator language
    return request.accept_languages.best_match(app.config["LANGUAGES"])
    """
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en'])
    """


def get_timezone():
    user = getattr(g, "user", None)
    if user is not None:
        return user.timezone


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)
    # babel.init_app(app, locale_selector=get_locale)

    from app.routes import main_bp

    app.register_blueprint(main_bp)

    return app
