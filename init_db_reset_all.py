#!/usr/bin/env python3

import subprocess
import shutil
import os
import sys


def copy_to_backup_file(file: str):
    path = os.path.join(os.getcwd(), file)
    if os.path.exists(path):
        path_backup = os.path.join(os.getcwd(), f"{file}.backup")
        try:
            shutil.copy(file, path_backup)
            print(f"File copied from {file} to {path_backup}")
        except Exception as e:
            print(f"Error copying file: {e}")
            sys.exit(1)


def delete_file(file: str):
    path = os.path.join(os.getcwd(), file)
    if os.path.exists(path):
        print(f"Try removing file [{path}] ...")
        try:
            os.remove(file)
            print(f"File [{path}] removed.")
        except Exception as e:
            print(f"ERROR when removing [{path}] : {e}")
            sys.exit(1)
    else:
        print(f"File [{path}] doesn't exists.")


def delete_folder(folder: str):
    path = os.path.join(os.getcwd(), folder)
    if os.path.exists(path):
        print(f"Try removing folder [{path}] ...")
        try:
            shutil.rmtree(folder)
            print(f"Folder [{path}] removed.")
        except Exception as e:
            print(f"ERROR when removing [{path}] : {e}")
            sys.exit(1)
    else:
        print(f"Folder [{path}] doesn't exists.")


def run_flask_commands():
    commands = [
        "flask db init",
        'flask db migrate -m "Initial migration"',
        "flask db upgrade",
    ]

    print("Try executing commands...")

    for cmd in commands:
        print(f"\nExecute: [{cmd}]")
        try:
            # shell=True permet d'exécuter la commande comme dans un terminal
            result = subprocess.run(cmd, shell=True, check=True, text=True)
            print(f"< success: {result.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"< error: {e}")
            sys.exit(1)

    print("\nAll command successfully executed.")


def remove_pycache():
    l: list = [
        "app/__pycache__",
        "app/api/__pycache__",
        "app/forms/__pycache__",
        "app/inc/__pycache__",
        "app/models/__pycache__",
        "app/routes/__pycache__",
    ]
    for p in l:
        print(f"-- Remove: [{p}] --")
        delete_folder(p)


if __name__ == "__main__":
    print("-" * 40)
    remove_pycache()
    print("-" * 40)
    print("-- Remove [migrations ] folder --")
    delete_folder("migrations")
    print("\n-- Remove db --")
    db_file = "app/data/app.db"
    copy_to_backup_file(db_file)
    delete_file(db_file)

    run_flask_commands()
