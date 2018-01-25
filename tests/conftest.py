"""Add custom options to py.test."""

import pytest


def pytest_addoption(parser):
    """Add option to recreate tox enviroments."""
    parser.addoption(
        "--recreate",
        action="store_true",
        default=False,
        help="Recreate the tox enviroments for click and toil modes.",
        )
