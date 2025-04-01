# initialize_app.py
import os
from app.config import basedir
from app.inc.tool_directory import clear_directory, remove_directory, create_directory


def initialize_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(basedir, "app", "data")
    migrations_dir = os.path.join(basedir, "migrations")

    print(
        f"""
------------------------------
-- Initialize the Flask app --
* Clear folder: {data_dir}
* Remove folder: {migrations_dir}
"""
    )

    clear_directory(data_dir)
    remove_directory(migrations_dir)
    create_directory(data_dir)

    print(
        """
------------------------------
"""
    )


if __name__ == "__main__":
    initialize_app()
