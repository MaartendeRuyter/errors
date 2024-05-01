"""Module to provide test methods for errors.enumerator module."""

import pytest

from errors.base import BaseEnumerator, ErrorCode, ErrorsClassErrors, add_error_data


def test_base_enumerators_class_exists():
    """Ensure ErrorsClassErrors class exists."""
    assert BaseEnumerator  # type: ignore


def test_keys_method_on_base_enumerators_class():
    """Test that base enumerator has keys method."""
    assert BaseEnumerator.keys() == []


def test_values_method_on_base_enumerators_class():
    """Test that base enumerator has values method."""
    assert BaseEnumerator.values() == []


def test_errors_class_errors_exists():
    """Ensure ErrorsClassErrors class exists."""
    assert ErrorsClassErrors  # type: ignore


def test_error_code_exists():
    """Ensure ErrorCode exists and inherits from tuple."""
    assert ErrorCode  # type: ignore


def test_error_code_has_mandatory_code_field():
    """Ensure ErrorCode has field code and description."""
    assert ErrorCode(code="TEST_001", description="TEST").code
    with pytest.raises(TypeError):
        assert ErrorCode(description="TEST")  # type: ignore


def test_error_code_has_mandatory_description_field():
    """Ensure ErrorCode has field code and description."""
    assert ErrorCode(code="TEST_001", description="TEST").description
    with pytest.raises(TypeError):
        assert ErrorCode(code="TEST_001")  # type: ignore


def test_error_code_has_optional_error_data_field():
    """Ensure ErrorCode has an optional error data field."""
    assert ErrorCode(code="TEST_001", description="TEST")
    assert ErrorCode(code="TEST_001", description="TEST", error_data={"data": "data"})


def test_add_error_data():
    """Adding error data to ErrorObject succesfull."""
    error = ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value
    error_data = {"data": "example"}
    assert add_error_data(error, error_data).error_data == error_data
