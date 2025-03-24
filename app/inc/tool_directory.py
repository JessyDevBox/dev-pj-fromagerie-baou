# app/inc/tool_directory.py
import os
import shutil


def create_directory(directory: str):
    """Create directory if doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Dir created: {directory}")
    else:
        print(f"Dir already exits: {directory}")


def clear_directory(directory: str):
    """Empty directory without remove it"""
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)  # remove all sub-folders
            else:
                os.remove(item_path)  # remove all files
        print(f"Dir is empty: {directory}")
    else:
        print(f"Dir not found: {directory}")


def remove_directory(directory: str):
    """Remove directory if exists"""
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Dir removed: {directory}")
    else:
        print(f"Dir not found: {directory}")
