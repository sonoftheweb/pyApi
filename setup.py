""" Init script for flask based api """
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = (
    "Boilerplate Flask API with Flask-RESTx, SQLAlchemy, pytest, flake8, "
    "tox, configured"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Jacob Ekanem"
AUTHOR_EMAIL = "prometheus6001@gmail.com"
PROJECT_URLS = {
    "Docs": "#",
    "Bugs": "#"
}
INSTALL_REQUIRES = [
    "Flask",
    "Flask-Bcrypt",
    "Flask-Cors",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "PyJWT",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "werkzeug==0.16.1",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8",
        "pre-commit",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-dotenv",
        "pytest-flake8",
        "pytest-flask",
        "tox",
    ]
}

setup(
    name="flask-api-tutorial",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="https://github.com/sonoftheweb/pyApi",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE
)
