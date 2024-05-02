"""Module to provide test methods for errors.error module."""

import pytest

from errors.base import BaseEnumerator, ErrorCode, ErrorsClassErrors, is_error
from errors.error import ListErrors


def test_list_errors_class_exists():
    """Ensure ErrorsClassErrors class exists."""
    assert ListErrors  # type: ignore


def test_list_error_is_singleton_class():
    """Ensure ErrorsClassErrors class is a singleton class."""
    list_errors = ListErrors()
    assert list_errors is ListErrors


def test_register_invalid_error_instance_error():
    """Test registering an invalid error raises exception."""
    with pytest.raises(ValueError):
        ListErrors.register_error(error_key="TEST", error="invalid_error_instance")  # type: ignore


def test_register_valid_error_instance_error():
    """Test registering an valid error is possible."""
    error = ErrorCode(code="TEST", description="desc")
    ListErrors.register_error(error_key="TEST", error=error)
    assert ListErrors.TEST == error  # type: ignore


def test_register_invalid_error_class_list_error():
    """Test registering an invalid error enumerator raises exception."""
    invalid_enumerator_class = BaseEnumerator
    with pytest.raises(ValueError):
        ListErrors.register_errors(errors=invalid_enumerator_class)  # type: ignore


def test_error_description_for_undefined_error_code_raises_exception():
    """Error_description for undefined error code raises exception."""
    non_existing_error_code = "non existing"
    with pytest.raises(KeyError):
        ListErrors.error_description(error_code=non_existing_error_code)


def test_error_description_retrieved_for_existing_error_code():
    """Retrieving error_description returns the correct description."""
    description = ListErrors.error_description(error_code="ER_GETERROR_00001")
    assert ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value.description == description


def test_is_error_returns_false():
    """
    Test is_error method returns False if error is not an instance off
    ErrorCode or subclass of ErrorCode.
    """
    assert not is_error("1")


def test_is_error_returns_true():
    """
    Test is_error method returns True if error is an instance of ErrorCode.
    """
    assert is_error(ErrorCode("code", "description"))


def test_is_error_returns_true_on_error_code_sub_class():
    """
    Test is_error method returns True if error is an instance of ErrorCode.
    """

    class ErrorCodeSubClass(ErrorCode):
        pass

    assert is_error(ErrorCodeSubClass("code", "description"))
