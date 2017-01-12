openweathermap-cli
==================

*A command line application for displaying weather details, written in Python.*

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

-  `Python`_

Installing
~~~~~~~~~~

Openweathermap-cli is on `PyPi`_ so it can be installed with pip.

.. code-block:: bash

    $ pip install openweathermap-cli

Using openweathermap-cli
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    Usage:
      weather today
      weather location [--set=<location>]
      weather -h | --help
      weather --version

Set your location

.. code-block:: bash

    $ weather location --set=<location>

Get today's weather forecast

.. code-block:: bash

    $ weather today

Example
~~~~~~~

Set the location to London and get today's weather details

.. code-block:: bash

    $ weather location --set=London,uk
    $ weather today

Built With
----------

-  `skele-cli`_
-  `Open Weather Map`_

Authors
-------

-  `Aziez Ahmed Chawdhary`_

License
-------

This project is licensed under the MIT License

.. _Open Weather Map: http://openweathermap.org/
.. _Python: https://www.python.org
.. _PyPi: https://pypi.python.org/pypi
.. _skele-cli: https://github.com/rdegges/skele-cli
.. _Aziez Ahmed Chawdhary: https://github.com/aziezahmed
