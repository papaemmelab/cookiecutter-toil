"""Add custom options to py.test."""


def pytest_addoption(parser):
    """Add option to recreate tox environments."""
    parser.addoption(
        "--tox-recreate",
        action="store_true",
        default=False,
        help="Recreate the tox environments for click and toil modes.",
        )

    parser.addoption(
        "--tox-develop",
        action="store_true",
        default=False,
        help="Run tox with --develop for click and toil modes (tests will run "
        "much faster!)."
        )

    parser.addoption(
        "--tox-pytest-args",
        default=None,
        type=str,
        help="Parameters to be passed to pytest inside tox "
        "(e.g. -s /tests/test_commands)."
        )

    parser.addoption(
        "--test-container",
        action="store_true",
        default=False,
        help="Run tox inside the project container."
        )
