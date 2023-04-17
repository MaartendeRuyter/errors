"""
Module to define the ErrorCode class and methods as well als the
FunctionalErrorsBaseClass enumerator

dataclass ErrorCode
-------------------

This data class defines the dedault error object that you can use
throughout your project. It contains the following attributes

- code (str) : the error code. Advice to make this code self
               explanatory using a naming convention
- description (str) : the error description

enumerator FunctionalErrorsBaseClass
------------------------------------

"""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Union


@dataclass(frozen=True)
class ErrorCode():
    """Immutable dataclass to define error codes."""
    code: str
    description: str
    error_data: Dict = field(default_factory=dict)


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
    Abstract enumerator for custom error codes
    Use this base class to define a set of custom error codes for your project.

    These errors can then be registered in one go.

    >>> from errors import ListErrors
    >>> ListErrors.register_errors(YourErrors)
    """
    pass


class ErrorsClassErrors(FunctionalErrorsBaseClass):
    """
    Class to define enumerator errors for Error module
    """
    COULD_NOT_FIND_ERROR_CODE = ErrorCode(
        code='ER_GETERROR_00001',
        description='Could not find requested error code')
