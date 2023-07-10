import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "rainfall_prediction"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/app_exception/__init__.py",
    f"src/{project_name}/app_exception/exception_handler.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Procfile",
    "requirements.txt",
    "setup.py"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, filename = os.path.split(filePath)
    if fileDir:
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory: {fileDir} for the file {filename}")
    
    if not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
        with open(filePath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
    else:
        logging.info(f"File already exists: {filename}")