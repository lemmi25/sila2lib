Changelog
=========

0.2.1
-----

*Authors:* Timm Severin (timm.severin@tum.de)

fdl\_parser.py
~~~~~~~~~~~~~~

-  ``FDLValidator`` has now a ``validate()`` function which can be used
   to validate FDL files.
-  Default value for string parameters does not include ``return_val``
   any more, this has been used in the auto-generated \_real.py
   \_simulation implementations. This has to be implemented manually as
   of now.
