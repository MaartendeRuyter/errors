=============
Error Manager
=============

A lightweight implementation of a manager for error messages throughout your
project. Allows you to easily define and register error codes and messages.
Enable easy access to a single list of registerd error codes and messages
throughout your project.

.. start-badges

.. list-table::
    :widths: 8 50
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |travis| |requires| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |commits-since|
  
.. |docs| image:: https://readthedocs.org/projects/errors/badge/?style=flat
    :target: https://errors.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/MaartendeRuyter/errors.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/MaartendeRuyter/errors

.. |requires| image:: https://requires.io/github/MaartendeRuyter/errors/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/MaartendeRuyter/errors/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/MaartendeRuyter/errors/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/MaartendeRuyter/errors

.. |version| image:: https://img.shields.io/pypi/v/error-manager.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/error-manager

.. |wheel| image:: https://img.shields.io/pypi/wheel/error-manager.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/error-manager

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/error-manager.svg
    :alt: Supported versions
    :target: https://pypi.org/project/error-manager

.. |commits-since| image:: https://img.shields.io/github/commits-since/MaartendeRuyter/errors/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/MaartendeRuyter/errors/compare/v0.1.0...master


.. end-badges


* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install error-manager

You can also install the in-development version with::

    pip install https://github.com/MaartendeRuyter/errors/archive/master.zip


Main usecases
=============
Error manager provides you with a ``ListErrors`` class to retrieve your
custom error codes and descriptions throughout your project::

    # retrieve customer defined ErrorCode object form ``ListErrors`` class
    >>> from errors import ListErrors
    >>> error = ListErrors.COULD_NOT_FIND_ERROR_CODE
    >>> error
    ErrorCode(code='ER_GETERROR_00001', description='Could not find requested 
    error code', error_data=<class 'dict'>)
    
    # add custom error data to error message when you want to persist or log
    # the error
    >>> from errors import add_error_data   
    >>> error_with_data = add_error_data(error, {'key': 'Example error data'})
    >>> error_with_data 
    ErrorCode(code='ER_GETERROR_00001', description='Could not find requested error code', error_data={'key': 'Example error data'})


Documentation
=============

https://errors.readthedocs.io/
