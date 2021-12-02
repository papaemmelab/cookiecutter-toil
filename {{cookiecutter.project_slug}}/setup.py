"""{{cookiecutter.project_slug}} setup.py."""

from os.path import join
from os.path import abspath
from os.path import dirname

from setuptools import find_packages
from setuptools import setup

ROOT = abspath(dirname(__file__))

# see 4 > https://packaging.python.org/guides/single-sourcing-package-version/
with open(join(ROOT, "{{cookiecutter.project_slug}}", "VERSION"), "r") as f:
    VERSION = f.read().strip()

setup(
    # single source package version
    version=VERSION,
    # in combination with recursive-includes in MANIFEST.in, non-python files
    # within the {{cookiecutter.project_slug}} will be copied into the
    # site-packages and wheels installation directories
    include_package_data=True,
    # return a list all Python packages found within the ROOT directory
    packages=find_packages(),
    # package-specific parameters
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.cli:main"
        ]
    },
    setup_requires=["pytest-runner>=5.3.1"],
    install_requires=[{% if cookiecutter.cli_type == 'toil' %}"toil_container>=2.0.0"{% else %}"click>=7.0"{% endif %}],
    extras_require={
        "test": [
            "coverage>=5.5.0",
            "pydocstyle>=6.1.1",
            "pytest-cov>=2.12.1",
            "pytest>=6.2.5",
            "pytest-env>=0.6.2",
            "pytest-sugar>=0.9.1",
            "pylint>=1.8.1",
            "requests>=2.18.4",
            "tox>=2.9.1",
        ]
    },
    author="{{cookiecutter.full_name}}",
    keywords=[],
    license="BSD",
    name="{{cookiecutter.project_slug}}",
    test_suite="tests",
    description="{{cookiecutter.project_description}}",
    long_description=(
        "📘 learn more of this project on [GitHub]"
        "(https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}})!"
    ),
    long_description_content_type="text/markdown",
    url="https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}",
)
