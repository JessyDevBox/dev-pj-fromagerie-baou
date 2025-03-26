# config.py
import os
import platform
from dotenv import load_dotenv

load_dotenv()


def get_platform_info():
    return {
        "os": platform.system(),  # Windows, Linux, Darwin (pour MacOS)
        "os_version": platform.version(),  # Version détaillée de l'OS
        "machine": platform.machine(),  # x86_64, armv7l (pour Raspberry Pi), etc.
        "processor": platform.processor(),  # Type de processeur
        "node": platform.node(),  # Nom de la machine
        "platform": platform.platform(),  # Description complète de la plateforme
        "python_version": platform.python_version(),  # Version de Python
    }


# from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
env_platform = os.environ.get("PLATFORM", "windows")


class ConfigEnv:
    is_prod = os.environ.get("APP_ENV", "dev") == "prod"
    platform = env_platform
    is_platform_windows = env_platform == "windows"
    is_platform_macos = env_platform == "macos"
    is_platform_raspberrypi = env_platform == "raspberrypi"
    flask_host = os.environ.get("FLASK_HOST", "0.0.0.0")
    flask_port = os.environ.get("FLASK_PORT", "5000")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data", "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY") or "csrf-secret-key"


class ConfigEmail:
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = os.environ.get("MAIL_PORT", 587)
    MAIL_SENDER = os.environ.get("MAIL_SENDER", "jessydevbox@gmail.com")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "azkgxtrjlvbsnpqk")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "false").lower() == "true"
