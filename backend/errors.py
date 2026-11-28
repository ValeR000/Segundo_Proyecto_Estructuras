class ProjectError(Exception):
    """Base class for every error of this project.

    The frontend can catch this single class to handle all project errors.
    """


class NotFoundError(ProjectError):
    """Something that was requested does not exist (e.g. an unknown vertex id)."""


class InvalidOperationError(ProjectError):
    """The operation is not allowed in the current state (e.g. rebuilding a bridge that is not destroyed)."""


class InvalidDataError(ProjectError):
    """A value is malformed or out of range (e.g. a duplicate id or a negative weight)."""
