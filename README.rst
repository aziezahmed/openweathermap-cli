openweathermap-cli
==================

|PyPI version|

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
      weather
      weather week
      weather -h | --help
      weather --version

Get today's weather forecast

.. code-block:: bash

    $ weather

Get the week's weather forecast

.. code-block:: bash

    $ weather week

Example
~~~~~~~

Get today's weather details

.. code-block:: bash

    $ weather 
    +-----------------------+------------+
    | City of Westminster   |            |
    |-----------------------+------------|
    | Temperature           | 10.45      |
    | Temp Max              | 12.0       |
    | Temp Min              | 9.0        |
    | Summary               | Rain       |
    | Detail                | light rain |
    | Sunrise               | 07:05:26   |
    | Sunset                | 17:23:52   |
    +-----------------------+------------+


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
.. |PyPI version| image:: https://img.shields.io/pypi/v/openweathermap-cli.svg
   :target: https://pypi.python.org/pypi/openweathermap-cli
