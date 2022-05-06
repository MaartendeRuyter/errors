
Changelog
=========

0.1.0 (2021-10-08)
------------------

* First release on PyPI.


0.9.0 (2021-10-11)
------------------

* added error codes as attribut to ListErrors class.
  After registration of an ErrorCode the errorcode is accessible in
  ``ListErrors`` via::

      ListErrors.ERROR_CODE_KEY

* Added Documentation and removed default redundant Documentation
  
1.0.0 (2021-10-12)
------------------

* Added Documentation and removed more default but redundant Documentation
* Added reference documentation for ``ListErrors`` and ``base`` module   

1.1.0 (2021-11-05)
------------------

* Added is_error method to check if an object is an instance of
  (sub)class ``ErrorCode``

1.1.1 (2021-11-06)
------------------

* Import ``ListErrors``, ``ErrorCode``, ``add_error_data()`` and ``is_error()``
  in ``errors`` ``__init__.py`` so that they can be directly imported from ``errors`` module

1.2.0 (2022-05-06)
------------------

* Added a dataclass ``ReturnValueWithStatus`` to allow consuming classes and
  methods to return a single return type with result, status and errors
  collected in one Object
