class GraphProjectError(Exception):
    """Base class for every error of this project.

    The frontend can catch this single class to handle all project errors.
    """


class NotFoundError(GraphProjectError):
    """Something that was requested does not exist (e.g. an unknown vertex id)."""


class InvalidOperationError(GraphProjectError):
    """The operation is not allowed in the current state (e.g. a duplicate vertex)."""


class InvalidDataError(GraphProjectError):
    """A value is malformed or out of range (e.g. a negative weight)."""
