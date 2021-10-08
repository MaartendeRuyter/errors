"""
Module to provide test methods for errors.error module
"""
from errors.cli import main
from collections import namedtuple

from errors.error import ListErrors

from errors.base import \
    ErrorsClassErrors, ErrorCode, BaseEnumerator


def test_main():
    assert main([]) == 0


def test_list_errors_class_exists():
    """Ensure ErrorsClassErrors class exists"""
    assert ListErrors

