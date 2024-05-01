"""
Module to provide test methods for ReturnValue dataclass of the errors module.
"""

import pytest

from errors.base import ErrorCode
from errors.data_classes import ReturnValueWithErrorStatus, ReturnValueWithStatus


def test_return_value_with_status_class_exists():
    """Ensure from ReturnValueWithStatus class exists."""
    assert ReturnValueWithStatus  # type: ignore


def test_return_value_with_error_status_class_exists():
    """Ensure ReturnValueWithErrorStatus class exists."""
    assert ReturnValueWithErrorStatus  # type: ignore


def test_return_value_with_status_has_result_attribute():
    """Ensure ErrorsClassErrors instance has result attribute."""
    assert hasattr(ReturnValueWithStatus(), "result")


def test_return_value_with_status_has_is_valid_attribute():
    """Ensure ErrorsClassErrors instance has _is_valid attribute."""
    assert hasattr(ReturnValueWithStatus(), "_is_valid")


def test_return_value_with_status_has_errors_attribute():
    """Ensure ErrorsClassErrors instance has errors attribute."""
    assert hasattr(ReturnValueWithStatus(), "errors")


def test_is_valid_attribute_is_true_if_there_are_no_errors():
    """Ensure is_valid property is true if there are no errors."""
    assert ReturnValueWithStatus().is_valid is True


def test_adding_errors_to_return_value():
    """test that errors can be added to a returnvalue object."""
    error = ErrorCode(code="TEST", description="desc")
    return_value = ReturnValueWithStatus()
    return_value.add_error(error)
    assert error in return_value._errors


def test_return_value_with_errors_is_invalid_by_default():
    """test a return value object with errors is by default invalid."""
    error = ErrorCode(code="TEST", description="desc")
    return_value = ReturnValueWithStatus()
    return_value.add_error(error)
    assert not return_value.is_valid


def test_return_value_can_remain_valid_when_adding_an_error():
    """test adding an error whilst keeping the status valid."""
    error = ErrorCode(code="TEST", description="desc")
    return_value = ReturnValueWithStatus()
    return_value.add_error(error, keep_current_status=True)
    assert return_value.is_valid


def test_return_value_remains_invalid_with_keep_current_status_set_to_true():
    """
    test adding an that when adding and error with keep_current_status set to
    true to a return value with status invalid doesn't change the status. I.e.
    status remains invalid.
    """
    error1 = ErrorCode(code="TEST1", description="desc")
    error2 = ErrorCode(code="TEST2", description="desc")
    return_value = ReturnValueWithStatus()
    assert return_value.is_valid
    return_value.add_error(error1)
    assert not return_value.is_valid
    return_value.add_error(error2, keep_current_status=True)
    assert not return_value.is_valid


def test_return_value_with_error_status_returns_error_value():
    """
    Test that ReturnValueWithErrorStatus returns a ReturnValueWithErrorStatus
    instance with an error and status invalid.
    """
    error = ErrorCode(code="TEST1", description="desc")
    return_value = ReturnValueWithErrorStatus(error)
    assert isinstance(return_value, ReturnValueWithStatus)
    assert error in return_value._errors
    assert not return_value.is_valid


def test_return_value_with_error_status_raises_type_error():
    """
    Test that ReturnValueWithErrorStatus returns a TypeError when
    the provided error is not of type ErrorCode.
    """
    error = "not an ErrorCode instance"
    with pytest.raises(TypeError):
        ReturnValueWithErrorStatus(error)  # type: ignore
