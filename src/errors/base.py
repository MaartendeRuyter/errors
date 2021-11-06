"""
Module to define enumerators for get_data module

enumerators:
    - BaseEnumerator
    - FunctionalErrorsBaseClass
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Union


@dataclass(frozen=True)
class ErrorCode():
    """Immutable dataclass to define error codes."""
    code: str
    description: str
    error_data: dict = dict


def is_error(error: Union[ErrorCode, Any]) -> bool:
    """Method to check in object is an instance of ErrorCode."""
    return issubclass(error.__class__, ErrorCode)


def add_error_data(error: ErrorCode, error_data: dict) -> ErrorCode:
    """Method to add error_data to and error object.

    :param error: error code object to be joined with error_data
    :type error: ErrorCode
    :param error_data: error data to be added to error code
    :type error_data: dict
    :returns:  ErrorCode -- New ErrorCode object with error_data added
    """
    return ErrorCode(
        code=error.code,
        description=error.description,
        error_data=error_data)


class BaseEnumerator(Enum):
    """
    Class to define base enumerator with values and keys methods
    Only to be used for defining new enumerators.
    """

    @classmethod
    def values(cls):
        return [item.value for item in list(cls.__members__.values())]

    @classmethod
    def keys(cls):
        return list(cls.__members__.keys())


class FunctionalErrorsBaseClass(BaseEnumerator):
    """
    Abstract class to define custom error code and message.
    """
    pass


class ErrorsClassErrors(FunctionalErrorsBaseClass):
    """
    Class to define enumerator errors for Error module
    """
    COULD_NOT_FIND_ERROR_CODE = ErrorCode(
        code='ER_GETERROR_00001',
        description='Could not find requested error code')
