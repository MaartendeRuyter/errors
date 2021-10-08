========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
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

.. |version| image:: https://img.shields.io/pypi/v/errors.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/errors

.. |wheel| image:: https://img.shields.io/pypi/wheel/errors.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/errors

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/errors.svg
    :alt: Supported versions
    :target: https://pypi.org/project/errors

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/errors.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/errors

.. |commits-since| image:: https://img.shields.io/github/commits-since/MaartendeRuyter/errors/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/MaartendeRuyter/errors/compare/v0.1.0...master



.. end-badges

Module to manage error code, descriptions and data in a unified way throughout a project

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install errors

You can also install the in-development version with::

    pip install https://github.com/MaartendeRuyter/errors/archive/master.zip


Documentation
=============


https://errors.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
