Framework files
======================

The files in this sub-package have mostly been generated or imported automatically. Please do not update the files manually, unless you really know what you are doing.

The tools to generate these files can be found in the `release tools </release_tools>`_.

protobuf
----------------------------------------

The protobuf files are automatically imported from the `sila\_base <https://gitlab.com/SiLA2/sila_base>`_ repository.

*Related tool:* `update_framework.py </release_tools/framework/update_framework.py>`_

schema
----------------------------------------

The schema files are automatically imported from the `sila\_base <https://gitlab.com/SiLA2/sila_base>`_ repository.

*Related tool:* `update_framework.py </release_tools/framework/update_framework.py>`_

feature_definitions/org.silastandard
----------------------------------------

The standard feature definitions files are automatically imported from the `sila\_base <https://gitlab.com/SiLA2/sila_base>`_ repository.

*Related tool:* `update_framework.py </release_tools/framework/update_framework.py>`_

feature_definitions/\*.py
-------------------------------------------

Most of these files are automatically generated from the feature definitions in the subdirectories of the feature_definition folder.

*Related tool:* `compile_standard_features.py </release_tools/framework/compile_standard_features.py>`_

.. note:: The `SimulationController` and the `SiLAService` feature have implementations (``SimulationController.py`` and ``SiLAService.py``) that have been written manually and also **need** to be updated manually in case the base files changes.

Framework and BinaryTransfer
---------------------------------------------

These files are created from the .proto files that are imported from the `sila\_base <https://gitlab.com/SiLA2/sila_base>`_ repository.

*Related tool:* `compile_framework.py </release_tools/framework/compile_framework.py>`_

.sila_base_commit_hash
----------------------------------------------

Contains the hash of the `sila\_base <https://gitlab.com/SiLA2/sila_base>`_ repository from which the framework files have been updated and is only used to check whether newer versions are available.

utilities.py
-----------------------------------------------

These are actually only utilities of the framework. Feel free to modify those if you deem necessary. Nothing auto-generated here.