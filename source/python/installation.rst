################
1. Installation
################

Install on WSL(Ubuntu22.04)
----------------------------

Python is already installed on your machine (the Linux Kernel is using it) - with version 3.10.
Because Python3.11 has a major performance improvement - we want it.

.. code-block:: bash

    # Add deadsnakes(from old versions of Python) repository
    # More information about deadsnakes https://github.com/deadsnakes/
    sudo add-apt-repository ppa:deadsnakes/ppa

    # Refresh the cache using the below command.
    sudo apt update 

    # And install Python 3.11 using the below command.
    sudo apt install python3.11 python3.11-venv -y

In order not to affect the Kernel, we use virtual environments.

Applications written in Python frequently use packages and modules that are not included in the standard library.
Applications will sometimes require a particular version of a library because they may need a specific issue to be solved or they may have been created using an outdated version of the library's interface.

Making a virtual environment—a self-contained directory tree including a Python installation for a certain version of Python and a number of additional packages—is the answer to this issue.

In Python we normally don't use as much docker when deploying/running applications - we use Virtual Environment

More about virtual environments: https://docs.python.org/3/tutorial/venv.html

.. code-block:: bash

   python3.11 -m venv venv
   source venv/bin/activate

   # Once in venv run
   python3.11
   
   # Write your hello world
   print("Hello World")

   # To exit
   # Control+D or write exit()

   # Care about the different version of Python
   # If you run
   python
   # or
   python3
   # or
   python3.10
   # or
   python3.11

   # That means our shebang will be different
   #!/usr/bin/env python3.11

Set Default Python Versions
----------------------------

.. note::

    You can install multiple versions of Python in Linux distros, but the default can only be one version.

.. warning::

    Make sure you know which applications depend on Python 3.10, because you can break some application

You can easily find it out using apt-cache rdepends command as below.

.. code-block:: bash

    apt-cache rdepends python3.10

Create symbolic links for the executable and set it up as default

.. code-block:: bash
    
    # Use update-alternatives to create symbolic links to python3
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2

    # And choose which one to use as Python3 via the command:
    sudo update-alternatives --config python3

Where to code
--------------

1. Python's embedded shell
+++++++++++++++++++++++++++

   Why???

2. Microsoft code
++++++++++++++++++

A powerful, lightweight free code editor with integrated tools to easily deploy your code to Azure. - https://code.visualstudio.com/

PRO:
    - lots of extensions
    - available Linux and Windows
    - can run code on WSL
    - support for Azure, docker and Kubernetes
CON:
    - some extensions are behind a paywall
    - you need to tune it before it's amazing

3. Jupyter Notebook
++++++++++++++++++++

JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality. - https://jupyter.org/

It's Python based so you need to install it using pip

.. code-block:: bash

    # If you have not created and activated venv
    python3.11 -m venv venv
    source venv/bin/activate
    
    # Install 
    pip install jupyter

    # Run
    jupyter notebook

    # Copy the link into a browser

PRO:
    - it allows you to start and play with code
    - is amazing for data science/ml or if you're trying to visualize data
    - can be run on a server and multiple people can access it
    - is embedded into Microsoft Code
CON:
    - it's not for OOP programming
    - hard to work if the feed will grow too much