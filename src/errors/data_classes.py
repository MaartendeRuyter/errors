"""_summary_"""

from dataclasses import dataclass, field
from typing import Any, List

import errors.settings as st

from .base import ErrorCode


@dataclass
class ReturnValueWithStatus:
    """
    Dataclass to define an object for returning results including status and
    errors from error class.

    """

    result: Any = None
    _is_valid: bool = True
    _errors: List[ErrorCode] = field(default_factory=list)

    @property
    def errors(self) -> List[ErrorCode]:
        return self._errors

    @property
    def is_valid(self) -> bool:
        return self._is_valid

    def add_error(self, error: ErrorCode, keep_current_status: bool = False) -> None:
        """Add and error to the return value instance.

        Args:
            error (ErrorCode): Error to be added
            keep_current_status (bool, optional):
                Will keep the is_valid status inchanged if set to True.
                Defaults to False.
        """
        self._errors.append(error)

        if not keep_current_status:
            self._is_valid = False


class ReturnValueWithErrorStatus:
    """Class to easuly define a ReturnValue with an errorcode.

    Should be used like:
    ReturnValueWithErrorStatus(error=predefined_error_code)

    returns an instance of ReturnValueWithStatus with predefined_error_code
    added to the error list.
    """

    def __new__(cls, error: ErrorCode):
        if not isinstance(error, ErrorCode):
            raise TypeError(st.EXC_ERROR_NOT_OF_ERROR_CODE_TYPE)
        return_value = ReturnValueWithStatus()
        return_value.add_error(error)
        return return_value
