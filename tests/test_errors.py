"""Module to provide test methods for errors.error module."""
import pytest

from errors.base import BaseEnumerator
from errors.base import ErrorsClassErrors
from errors.cli import main
from errors.error import ListErrors


def test_main():
    assert main([]) == 0


def test_list_errors_class_exists():
    """Ensure ErrorsClassErrors class exists."""
    assert ListErrors


def test_list_error_is_singleton_class():
    """Ensure ErrorsClassErrors class is a singleton class."""
    list_errors = ListErrors()
    assert list_errors is ListErrors


def test_register_invalid_error_class_list_error():
    """Test registering an invalid error enumerator raises exception."""
    invalid_enumerator_class = BaseEnumerator
    with pytest.raises(ValueError):
        ListErrors.register_errors(errors=invalid_enumerator_class)


def test_error_description_for_undefined_error_code_raises_exception():
    """Error_description for undefined error code raises exception."""
    non_existing_error_code = 'non existing'
    with pytest.raises(KeyError):
        ListErrors.error_description(error_code=non_existing_error_code)


def test_error_description_retrieved_for_existing_error_code():
    """Retrieving error_description returns the correct description."""
    description = ListErrors.error_description(error_code='ER_GETERROR_00001')
    assert ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value.description == \
        description
