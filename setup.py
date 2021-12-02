"""cookiecutter-toil setup.py."""
from setuptools import find_packages
from setuptools import setup

setup(
    # the version is only defined in one place
    version="2.0.0",
    # in combination with recursive-includes in MANIFEST.in, non-python files
    # included inside the {{cookiecutter.project_slug}} will be copied to the
    # site-packages installation directory
    include_package_data=True,
    # return a list all Python packages found within the ROOT directory
    packages=find_packages(),
    # package-specific parameters
    author="Juan S. Medina, Juan E. Arango",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Topic :: Utilities",
    ],
    install_requires=["cookiecutter>=1.7.3"],
    setup_requires=["pytest-runner>=5.3.1"],
    extras_require={
        "test": [
            "pytest-cov>=2.12.1",
            "binaryornot>=0.4.4",
            "pytest>=6.2.5",
            "pytest-cookies>=0.6.1",
            "tox>=3.24.3",
        ]
    },
    keywords=["cookiecutter", "toil"],
    license="BSD",
    name="cookiecutter-toil",
    description="🍪 A cookiecutter for the creation of toil pipelines.",
    long_description=(
        "📘 learn more about this project on "
        "[GitHub](https://github.com/papaemmelab/cookiecutter-toil)!"
    ),
    long_description_content_type="text/markdown",
    url="https://github.com/papaemmelab/cookiecutter-toil",
)
