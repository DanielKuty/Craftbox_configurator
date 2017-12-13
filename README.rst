========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/Craftbox_configurator/badge/?style=flat
    :target: https://readthedocs.org/projects/Craftbox_configurator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/DanielKuty/Craftbox_configurator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/DanielKuty/Craftbox_configurator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/DanielKuty/Craftbox_configurator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/DanielKuty/Craftbox_configurator

.. |requires| image:: https://requires.io/github/DanielKuty/Craftbox_configurator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/DanielKuty/Craftbox_configurator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/DanielKuty/Craftbox_configurator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/DanielKuty/Craftbox_configurator

.. |version| image:: https://img.shields.io/pypi/v/craftbox-configurator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/craftbox-configurator

.. |commits-since| image:: https://img.shields.io/github/commits-since/DanielKuty/Craftbox_configurator/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/DanielKuty/Craftbox_configurator/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/craftbox-configurator.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/craftbox-configurator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/craftbox-configurator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/craftbox-configurator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/craftbox-configurator.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/craftbox-configurator


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install craftbox-configurator

Documentation
=============

https://Craftbox_configurator.readthedocs.io/

Development
===========

To run the all tests run::

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
