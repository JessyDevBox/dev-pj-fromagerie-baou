from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import Config

# Initialisation des extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions avec l'application
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Configuration de LoginManager
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."
    login_manager.login_message_category = "info"

    # Enregistrement des blueprints
    from app.routes import main_bp, auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
