========
Contents
========


Error-manager: Managing error codes throughout you project
==========================================================


**Error-manager** is a simple library for Python to manage all your projects error codes.

-------------------

**errors manager main use cases **::

    # retrieve error message from error code
    >>> from errors.error import ListErrors
    >>> ListErrors.error_description('ER_GETERROR_00001')
    'Could not find requested error code'

    # add custom error data to error message
    >>> from errors.base import ErrorsClassErrors
    >>> from errors.base import add_error_data
    >>> error = ErrorsClassErrors.COULD_NOT_FIND_ERROR_CODE.value
    >>> error
    ErrorCode(code='ER_GETERROR_00001', description='Could not find requested 
    error code', error_data=<class 'dict'>)
    
    >>> error_with_data = add_error_data(error, {'key': 'Example error data'})
    >>> error_with_data 
    ErrorCode(code='ER_GETERROR_00001', description='Could not find requested error code', error_data={'key': 'Example error data'})


    
    # add custom messages to ListErrors (see chapter create custom error classes)
    >>> ListErrors.register_errors(<CustomErrorClassEnumerator>)
    
    >>> r.encoding
    'utf-8'
    >>> r.text
    '{"type":"User"...'
    >>> r.json()
    {'private_gists': 419, 'total_private_repos': 77, ...}

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   reference/index
   contributing
   authors
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
