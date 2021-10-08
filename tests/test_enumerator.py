"""
Module to provide test methods for errors.enumerator module
"""
import pytest
from errors.base import \
    ErrorsClassErrors, ErrorCode, BaseEnumerator


def test_base_enumerators_class_exists():
    """Ensure ErrorsClassErrors class exists"""
    assert BaseEnumerator


def test_keys_method_on_base_enumerators_class():
    """Test that base enumerator has keys method """
    assert BaseEnumerator.keys() == []


def test_values_method_on_base_enumerators_class():
    """Test that base enumerator has values method """
    assert BaseEnumerator.values() == []


def test_errors_class_errors_exists():
    """Ensure ErrorsClassErrors class exists"""
    assert ErrorsClassErrors


def test_error_code_exists():
    """Ensure ErrorCode exists and inherits from tup;e"""
    assert ErrorCode


def test_error_code_has_mandatory_code_field():
    """Ensure ErrorCode has field code and description"""
    assert ErrorCode(code='TEST_001', description='TEST').code
    with pytest.raises(TypeError):
        assert ErrorCode(description='TEST')


def test_error_code_has_mandatory_description_field():
    """Ensure ErrorCode has field code and description"""
    assert ErrorCode(code='TEST_001', description='TEST').description
    with pytest.raises(TypeError):
        assert ErrorCode(code='TEST_001')


def test_error_code_has_optional_error_data_field():
    """Ensure ErrorCode has an optional error data field"""
    assert ErrorCode(code='TEST_001', description='TEST')
    assert ErrorCode(code='TEST_001', description='TEST', error_data='data')
