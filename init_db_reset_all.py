#!/usr/bin/env python3

import subprocess
import shutil
import os
import sys


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


if __name__ == "__main__":
    run_flask_commands()
