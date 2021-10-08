"""Module to define ListErrors class."""
from errors.base import ErrorCode
from errors.base import ErrorsClassErrors
from errors.base import FunctionalErrorsBaseClass


class ListErrors():
    _errors = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_errors(cls, errors: FunctionalErrorsBaseClass) -> None:
        """Class method to register new errors."""
        if not issubclass(errors, FunctionalErrorsBaseClass):
            raise ValueError(
                'provide errors are not of type FunctionalErrorsBaseClass')
        for key in errors.keys():
            error = errors[key].value
            cls._errors.update({error.code: error.description})

    @classmethod
    def error_description(cls, error_code: str) -> str:
        """Transforms error code in error description."""
        error = cls._errors.get(error_code)
        if not error:
            raise KeyError(cls.error_object(
                ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value
            ))
        return error

    @staticmethod
    def error_object(error_code: ErrorCode) -> dict:
        return {
            'error': error_code.code,
            'description': error_code.description
        }


ListErrors.register_errors(ErrorsClassErrors)
