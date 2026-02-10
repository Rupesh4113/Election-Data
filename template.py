import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

print("Running from:", Path.cwd())

for file in list_of_files:
    path = Path(file)

    # create parent dirs
    path.parent.mkdir(parents=True, exist_ok=True)

    # create file if missing
    if not path.exists():
        path.touch()
        logging.info(f"CREATED → {path.resolve()}")
    else:
        logging.info(f"EXISTS → {path.resolve()}")
