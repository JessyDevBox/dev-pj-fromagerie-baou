# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import Config
from app.inc.mail import init_mail

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Configure LoginManager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."
    login_manager.login_message_category = "info"

    migrate.init_app(app, db)

    # Initialize mail object
    init_mail(app)

    # Import et enregistrement des blueprints
    from app.routes.main import bp as main_bp
    from app.routes.garden import bp as garden_bp
    from app.routes.auth import bp as auth_bp
    from app.routes.admin import bp as admin_bp
    from app.routes.sandbox import bp as sandbox_bp
    from app.routes.sensor import bp as sensor_bp
    from app.api.endpoints import bp as api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(garden_bp, url_prefix="/garden")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(sensor_bp, url_prefix="/sensor")
    app.register_blueprint(sandbox_bp, url_prefix="/sb")
    app.register_blueprint(api_bp, url_prefix="/api")

    @login_manager.user_loader
    def load_user(id):
        # from app.models.models import User
        from app.models import User

        return User.query.get(int(id))

    return app
