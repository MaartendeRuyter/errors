"""
Module to define ListErrors class
"""
from errors.base import ErrorCode
from errors.base import ErrorsClassErrors
from errors.base import FunctionalErrorsBaseClass


class ListErrors():
    _errors = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_errors(cls, errors):
        if not issubclass(errors, FunctionalErrorsBaseClass):
            raise ValueError('no good class')
        for key in errors.keys():
            error = errors[key].value
            cls._errors.update({error.code: error.description})

    @classmethod
    def error_description(cls, error_key: str) -> str:
        error = cls._errors.get(error_key)
        if not error:
            raise KeyError(cls.error_object(
                ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE
            ))
        return error

    @staticmethod
    def error_object(error_code: ErrorCode) -> dict:
        return {
            'error': error_code.code,
            'description': error_code.description
        }


ListErrors.register_errors(ErrorsClassErrors)
