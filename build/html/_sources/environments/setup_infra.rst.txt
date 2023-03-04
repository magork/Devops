##################################
3. Setup developing infrastructure
##################################

=============
Prerequisites
=============

.. note::

    You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11.

## Install WSL
==============

Run the command in an administrator PowerShell or Windows Command Prompt and then restart your machine.

.. code-block:: bash

    wsl --install

    # Some of Windows distributions have obsolete packages, you need to specify the distribution name
    wsl --install -d Ubuntu

    # By default, it will install Ubuntu, to install a different distribution 
    # To see a list of available Linux distributions available for download through the online store, enter:

    wsl --list --online 
    # or

    wsl -l -o.

    # To install additional Linux distributions after the initial install, you may also use the command:
    wsl --install -d <Distribution Name>.

======================
Install Docker Desktop
======================

Open https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe then run the installer.

.. code-block:: bash

    # Create a fedora docker container
    docker run -it fedora bash

    # install utilities on the container (for normal virtual machines we don't need to install them)
    dnf install util-linux tree passwd

To find what distribution and version of Linux are you running

.. code-block:: bash

    cat /etc/os-release

===============
Install VS Code
===============

Install VS Code https://code.visualstudio.com/Download To be able to run code directly on the WSL we need the WSL Extension

The Linux command line is a text interface to your computer. Often referred to as the shell, terminal, console, prompt or various other names,

========================
Setup WSL - Ubuntu 22.04
========================

I decided to upgrade my wsl to the latest version Ubuntu 22.04

These are the steps that I took:

1. Backup my information (I pushed all the code to git)

2. Stop and remove the wsl

.. code-block:: bash

    wsl --shutdown

    wsl --unregister Ubuntu

    wsl --install -d Ubuntu

3. Access the WSL - setup a new user and password

4. Update all the packages

.. code-block:: bash

    sudo apt update 

    sudo apt upgrade -y

Install packages

.. code-block:: bash

    sudo apt install vim python3.11-venv make -y

5. Disabled password request for my user when running sudo

.. code-block:: bash

    sudo su

Update the ``/etc/sudoers`` file using ``vim /etc/sudoers``:

.. code-block:: bash

    %sudo   ALL=(ALL:ALL) ALL

to

.. code-block:: bash

    %sudo   ALL=(ALL:ALL) NOPASSWD:ALL


Save, you need to use ``wq!`` don't forget the ``!``.

6. Update the ``~/.bashrc`` with aliases for root and your user

.. code-block:: bash

    alias ll='ls -ltrha --color=auto' # add arguments to a command that exists

    alias ls='ls -ltrha --color=auto' # add arguments to a command that exists

    alias vi='vim' # redirect the old application to the new one

    alias exot='exit' # correct typing errors

    alias clera='clear' # correct typing errors

    alias qpositive='history -c && history -w && exit' # link more commands under one

    alias bing='git push'

    alias bang='git status && git add --all && git commit -m'

    alias qqqRunEnv='. venv/bin/activate'

    alias eeeCreateVEnv='python3 -m venv venv'

    alias duck='cd /home/${USER}/sandbox'

    alias shit='sudo $(history -p \!\!)'

    export PATH="$PATH:/home/${USER}/sandbox"

after the update of the aliases you need to source them to have them available run ``source ~/.bashrc``
 
7. Create your sandbox

.. code-block:: bash

    mkdir -p /home/${USER}/sandbox
    duck

8. Create an ssh-key for the machine

.. code-block:: bash

    ssh-keygen -t ed25519 -C "${USER}@$(hostname)"

read the newly created key

.. code-block:: bash

    cat ~/.ssh/id_ed25519.pub

and add it in the GitHub https://github.com/settings/keys

9. Configure git

.. code-block:: bash

    git config --global user.email "<MAIL>"

    git config --global user.name "<USER>"

    git config --global core.editor vim

10. Clone all your projects
