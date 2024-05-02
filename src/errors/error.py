"""Module to define ListErrors class."""

from typing import Dict, Type

from errors.base import ErrorCode, ErrorsClassErrors, FunctionalErrorsBaseClass


class ListErrors:
    """Singleton Class for registering and retrieving error codes"""

    _errors: Dict[str, str] = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_error(cls, error_key: str, error: ErrorCode) -> None:
        """Class method to register a single error key with error code."""
        if not isinstance(error, ErrorCode):
            raise ValueError("provided error is not of type ErrorCode")
        cls._errors.update({error.code: error.description})
        setattr(cls, error_key, error)

    @classmethod
    def register_errors(cls, errors: Type[FunctionalErrorsBaseClass]) -> None:
        """Register list of errors defined in a FunctionalErrorsBaseClass

        :param errors: The class containg the errors (not an instance of that class)
        :type errors: Type[FunctionalErrorsBaseClass]
        :raises ValueError: raises ValueError when
        """
        if not issubclass(errors, FunctionalErrorsBaseClass):
            raise ValueError("provide errors are not of type FunctionalErrorsBaseClass")
        for error_key in errors.keys():
            error = errors[error_key].value
            cls.register_error(error_key=error_key, error=error)

    @classmethod
    def error_description(cls, error_code: str) -> str:
        """Transforms error code in error description."""
        error = cls._errors.get(error_code)
        if not error:
            raise KeyError(
                cls.error_object(ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value)
            )
        return error

    @staticmethod
    def error_object(error_code: ErrorCode) -> dict:
        """Transforms error code into dict."""
        return {"error": error_code.code, "description": error_code.description}


ListErrors.register_errors(ErrorsClassErrors)
