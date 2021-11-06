=====
Usage
=====
The error-manager module provides your project with
	- a single way to define and register a default project error code
	- add specific error data to a default error code when needed
	- a enumator class to group errors for a specific domain in your project
	- a ErrorList class to retrieve error descriptions from error codes


Defining an error code
----------------------
The error-manager package provide a simple non mutable dataclass ErrorCode
that should be used to define error codes::

	from errors import ErrorCode

	MY_DEFAULT_ERROR_CODE = ErrorCode(
		code='ERR_MYERR_0001',
		description='my default error code'
	)

Register an error code
----------------------
Once the error code is defined it can be registered against the ``ListErrors``
class using ``register_error()`` ::

	from errors import ListErrors

	ListErrors.register_error(
	    error_key = 'MY_DEFAULT_ERROR_CODE',
	    error  = MY_DEFAULT_ERROR_CODE
	)


Retrieving an error code
------------------------
After registration the ``ErrorCode`` instance be retrieved from the
``ListErrors`` class using the ``error_key`` throughout your project::

	 from errors import ListErrors
	 error = ListErrors.MY_DEFAULT_ERROR_CODE


Retrieving error description
----------------------------
In case you have only persisted the error code without the error description
you can use ``ListErrors`` class method ``error_description`` to retrieve the
error description.::

	>>> from errors import ListErrors
	>>> ListErrors.error_description('ERR_MYERR_0001')
	'my default error code'


Enumarator with error Codes
---------------------------
When needed you can group a set of error codes for a specific part of your
project by using ``FunctionalErrorsBaseClass``::

	from errors.base import FunctionalErrorsBaseClass

	class MyErrors(FunctionalErrorsBaseClass):
	    """Class to define enumerator with functional errors."""
	    CONNECTIVITY_ERROR = ErrorCode(
	        code='GD_NETW_0001',
	        description='Network connectivity issues')

	    INVALID_XML_IN_RESPONSE = ErrorCode(
	        code='GD_CONV_00201',
	        description='Response contains invalid XML')

	    INVALID_JSON_IN_RESPONSE = ErrorCode(
	        code='GD_CONV_00101',
	        description='Response contains invalid JSON')

Register an ErrorCodes enumerator
---------------------------------
This class can then be registered in one go against the ``ListErrors`` class
using class method ``register_errors()``::

	>>> from errors import ListErrors
	>>> ListErrors.register_errors(MyErrors)
	>>> ListErrors.CONNECTIVITY_ERROR
	ErrorCode(code='GD_NETW_0001', description='Network connectivity issues',
	error_data=<class 'dict'>)


Adding data to the error
------------------------
When specific data needs to be added to the error you can use
``add_error_data()`` to add data to the non mutable ``ErrorCode`` instance::

	>>> from errors import ListErrors, add_error_data
	>>> the_error = ListErrors.UNEXPECTED_404_RESPONSE
	>>> add_error_data(
		error=the_error,
		error_data={'url_called': 'www.url.com'})
	>>> the_error
	ErrorCode(code='GD_RESP_0004', description='URL returned unexpected 404
	response', error_data={'url_called': 'www.url.com'})


Check if an object is of (sub)class ErrorCode
---------------------------------------------
When you want to check if a return value is either an error_code
you can use ``is_error()``. This method checks if an object is of class ``ErrorCode`` or a subclass there of::

	>>> from errors import ListErrors, is_error
	>>> the_error = ListErrors.UNEXPECTED_404_RESPONSE
	>>> is_error(the_error)
	True
	>>> is_error({'data': 'or_any_other_object')}
	False
