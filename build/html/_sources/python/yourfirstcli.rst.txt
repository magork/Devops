###################
8. Your first CLI
###################

Create directory and files structure.

::

    cli  # directory project
    ├── devops_cli  # directory package
    │   ├── __init__.py
    │   └── devops_cli.py  # your script
    └── setup.py

.. note::
    
    The Python interpreter is informed that a directory contains code for a Python module by the ``__init__.py`` file.
    A file named ``__init__.py`` may be empty.
    You cannot import modules into your project from another location without one. 