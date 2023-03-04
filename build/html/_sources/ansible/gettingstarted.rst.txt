##################
3. Getting Started
##################

We will install Docker in WSL (there are some problems with getting the network working between wsl and docker containers)

.. code-block:: bash

    # 
    sudo apt-get update
    sudo apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    sudo apt-get update
    sudo apt-get -y install docker-ce docker-ce.cli containerd.io

    sudo service docker start # Run docker service

    docker run --name managed_node1 ubuntu

    docker ps

    # Find out IPAddress
    docker inspect -f "{{ .NetworkSettings.IPAddress }}" nginx

    # or
    docker exec -it managed_node1 bash
    hostname -I

    # To access via SSH server it needs SSH server installed
    apt update && apt -y install openssh-server

    # allow to login as root account via SSH.
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

    # change the password for the account
    passwd

    # start the SSH service on the container.
    /etc/init.d/ssh start

    # check that the service is running 
    /etc/init.d/ssh status

.. note::

    Ansible is being used to configure virtual machines, we can configure containers (normally we create an image that we will reuse)

There are 2 ways of running Ansible:

#. Adhoc commands

.. code-block:: bash

    # This command will check if you have a connection to the managed nodes
    ansible localhost -m ping

    # This command will allow you to run a shell session on the managed node
    ansible localhost -m shell "hostname"

    ansible --version

#. Playbook

For this course, we will use containers.

.. code-block:: bash 

