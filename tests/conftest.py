"""Add custom options to py.test."""

import pytest


def pytest_addoption(parser):
    """Add option to recreate tox environments."""
    parser.addoption(
        "--recreate",
        action="store_true",
        default=False,
        help="Recreate the tox environments for click and toil modes.",
        )
