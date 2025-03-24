# run.py
from app import create_app, db
from app.config import ConfigEnv

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    print(f"*** IS PROD: {ConfigEnv.is_prod} ***")

    host = ConfigEnv.flask_host
    port = ConfigEnv.flask_port

    if ConfigEnv.is_prod:
        print(f"*** PROD - host:port - {host}:{port} ***")
        app.run(host=host, port=port)
    else:
        print(f"*** DEV - host:port - {host}:{port} ***")
        if host:
            app.run(debug=True, host=host, port=port)
        else:
            app.run(debug=True)
