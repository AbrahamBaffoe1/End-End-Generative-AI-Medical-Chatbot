#  This template will create the entire project structure for a python project
#  run this file to create the project structure

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(levelname)s: %(message)s')
logging.debug('Start of program')

# lis of folders to create nd files to create
list_of_folders = [
    '.github/workflows',
    'src'
]

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'research/trials.ipynb',
    'src/prompt.py',
    '.gitignore',
    '.env',
    'Dockerfile',
    'requirements.txt',
    'main.py',
    'setup.py',
    'app.py',
    'config.yaml',
    'test.py',
    'pyproject.toml',
    'README.md',
]

#  creating files and checking if they are empty or not
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

#  creating folders and checking if they are empty or not
for folder in list_of_folders:
    filepath = Path(folder)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")