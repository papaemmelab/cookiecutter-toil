"""{{cookiecutter.project_slug}} specific exceptions."""


class ValidationError(Exception):

    """A class to raise when a validation error occurs."""


class MissingRequirementError(Exception):

    """A class to raise when a requirement is missing."""


class MissingOutputError(Exception):

    """A class to raise when a file that should exist is missing."""


class ConfigurationError(Exception):

    """A class to raise when is not properly configured."""


class ImplementationError(Exception):

    """A class to raise when is not properly implemented."""


class CantBeRunError(Exception):

    """A class to raise when a pipeline just cannot be run."""


class MissingDataError(Exception):

    """A class to raise when data is missing."""
