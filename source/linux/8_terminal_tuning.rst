##################
8. Terminal tuning
##################

=======
Aliases
=======

The alias command makes it possible to launch any command or group of commands (with arguments, options, or redirection) by entering a pre-set string.

Update user profile ``.bashrc``, ``bash_profile`` or ``.profile``

.. code-block:: bash

    # add arguments to a command that exists
    alias ll='ls -ltrha --color=auto'

    # add arguments to a command that exists
    alias ls='ls -ltrha --color=auto'

    # redirect the old application to the new one
    alias vi='vim'

    # correct typing errors
    alias exot='exit'

    # correct typing errors
    alias clera='clear'

    # link more commands under one
    alias qpositive='history -c && history -w && exit'

    alias bing='git push'
    alias bang='git status && git add --all && git commit -m'

    # go to the sandbox
    alias duck='cd /home/devx/sandbox'

    # activate python virtual environment
    alias qqqRunVEnv='. venv/bin/activate'

    # create python virtual environment
    alias eeeCreateVEnv='python3 -m venv venv'

    # run last command as root
    alias zzz='sudo $(history -p \!\!)'

========
The fuck
========

``TheFuck`` is a magnificent app that corrects errors in previous console commands.

.. code-block:: bash

    # create python environment
    python3 -m venv venv

    # source python environment
    . venv/bin/activate

    # install thefuck python library
    pip install thefuck

Update user profile ``.bashrc``, ``bash_profile`` or ``.profile``

.. code-block:: bash

    eval $(thefuck --alias FUCK)

=========================
Run sudo without password
=========================

Update the ``/etc/sudoers`` file:

.. code-block:: bash

    %sudo   ALL=(ALL:ALL) ALL

to

.. code-block:: bash

    %sudo   ALL=(ALL:ALL) NOPASSWD:ALL
