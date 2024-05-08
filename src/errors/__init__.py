"""init file errors module."""

__version__ = "1.3.5"

from errors.base import add_error_data, is_error  # noqa F401
from errors.data_classes import ReturnValueWithErrorStatus  # noqa F401
from errors.data_classes import ReturnValueWithStatus  # noqa F401
from errors.error import ErrorCode, ListErrors  # noqa F401
