import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ == "0.0.0"

REPO_NAME = "Election-Data"
AUTHOR_USER_NAME = "Rupesh"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "amerupesh08@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    VERSION=__Version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    Long_Description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    }
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

cpnda create -n venv python=3.14.2