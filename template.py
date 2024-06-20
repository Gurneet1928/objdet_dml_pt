import os
from pathlib import Path
import logging

#For Project Template Creation

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'PyTorch_Object_Detection'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/model_components/__init__.py",
    f"src/{project_name}/project_modules/__init__.py"
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "trail_runs/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Directory created: {file_dir} for file : {file_name}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as file:
            logging.info(f"Empty File created: {filepath}") 
    else:
        logging.info(f"File already exists: {filepath}")
