"""init file errors module."""

__version__ = "1.4.3"

from errors.base import FunctionalErrorsBaseClass, add_error_data, is_error
from errors.data_classes import ReturnValueWithErrorStatus, ReturnValueWithStatus
from errors.error import ErrorCode, ListErrors
from errors.mixin import ErrorListByMixin

__all__ = [
    "add_error_data",
    "is_error",
    "ReturnValueWithErrorStatus",
    "ReturnValueWithStatus",
    "ErrorCode",
    "ListErrors",
    "ErrorListByMixin",
    "FunctionalErrorsBaseClass",
]
