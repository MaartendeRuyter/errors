"""_summary_
"""
from dataclasses import dataclass, field
from typing import Any, List

from .base import ErrorCode


@dataclass
class ReturnValueWithStatus():
    """
    Dataclass to define an object for returning results including status and
    errors from error class.

    """
    _result: Any = None
    _is_valid: bool = True
    _errors: List[ErrorCode] = field(default_factory=list)

    @property
    def result(self):
        return self._result

    @property
    def errors(self):
        return self._errors

    @property
    def is_valid(self):
        return self._is_valid

    def add_error(self, error: ErrorCode, keep_current_status: bool = False):
        """Add and error to the return value instance.

        Args:
            error (ErrorCode): _description_
            keep_current_status (bool, optional):
                Will . Defaults to False.
        """
        self._errors.append(error)

        if not keep_current_status:
            self._is_valid = False
