from app import create_app
from app.config import Config
from app.models import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    host = Config.FLASK_HOST
    port = Config.FLASK_PORT
    print(f"----- APP Name: {Config.APP_NAME} -----")
    print(f"*** ENV: {Config.ENV} *** PROD - host:port - {host}:{port} ***")

    if Config.ENV == "production":
        app.run(host=host, port=port)
    else:
        if host:
            app.run(debug=True, host=host, port=port)
        else:
            app.run(debug=True)
