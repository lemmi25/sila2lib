Tests FDLParser
===============

This directory contains tests regarding the FDLParser classes and functions.

*Note*: As of writing this, the test cases do not claim to be comprehensive, but rather a subset of possible applications.

Executing
---------

Requirements
~~~~~~~~~~~~

It is recommended to use ``nose2`` to run and analyse the tests. To install ``nose2``, run

.. code-block:: console

    pip install nose2


Running the tests
~~~~~~~~~~~~~~~~~

To execute all unittests in the ``FDLParser`` package open a terminal, make sure you are in the ``FDLParser`` directory and run one of the following commands:

.. code-block:: console

    # Simple unittest of the modules, will
    nose2

    # Generate a coverage report in the terminal
    nose2 --with-overage

    # Generate a coverage report in HTML format, can be used to
    #   show which lines are covered:
    nose2 --with-coverage --coverage-report html

For more information on the usage please refer to the official `nose2 <https://docs.nose2.io/en/latest/>`_ documentation.

