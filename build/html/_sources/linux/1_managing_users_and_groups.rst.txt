############################
1. Managing Users and Groups
############################

For an authorized person to gain access to the system, a user account must be created on the system. User and group account information is stored in several files:

.. code-block:: bash

    /etc/passwd
    /etc/shadow
    /etc/group
    /etc/gshadow

===========
/etc/passwd
===========

The ``/etc/passwd`` file contains all user's properties. Each line contains information about one user account. There are seven fields per line entry separated by a colon (:).

.. code-block:: bash

    user_name:x:UID:GID:comments:home_directory:shell

    # user_name: `/^[a-z0-9-*]+$/`. Should not use uppercase letters or special characters
    # x: password placeholder
    # UID: a unique number. UIDs between 0 and 999 are reserved for system accounts
    # GID: a number that corresponds with a group entry in /etc/group
    # comments: info about the user
    # home_directory: the default location is /home/user_name
    # shell: user's default shell

===========
/etc/shadow
===========

This file stores the encrypted user's password along with other info.

.. code-block:: bash

    user_name:encrypted_passwords:lastchg_days:min_days:max_days:warn_days:inactive_days:disabled_days:

    # user_name: `/^[a-z0-9-*]+$/`. Should not use uppercase letters or special characters
    # encrypted_passwords: May be empty. An exclamation mark shows that the user is locked
    # lastchg_days: number of days in epoch time since the password was changed
    # min_days: minimum number of days that must pass before the user can change the passwords
    # max_days: maximum number of days before the user gets password expiration warnings
    # warn_days**: number of days for which the user gets password expiration warnings
    # inactive_days: maximum number of days for user inactivity
    # disabled_days: number of days in epoch time after which the account expires

Most of the above parameters can be changed with **password**, **usermod**, and/or **chage** commands.

==========
/etc/group
==========

This file contains group information. Every user must be a member of at least one group, which is called *the primary group*. Additional groups may be created and users assigned to them.

.. code-block:: bash

    group_name:x:GID:user_list

    # group_name: a unique group name
    # x: password placeholder. Usually, group passwords are not used. It may contain an encrypted password
    # GID: the group ID
    # user_list: a comma-delimited list of users assigned to the group. The user's primary group is defined in /etc/password

===================
Configuration files
===================

The files mentioned above contain only user and group information and attributes. There are additional files/directories that configure default values for various attributes.

.. code-block:: bash

    /etc/default/useradd
    /etc/login.defs
    /etc/skel/

===============
User management
===============

Normally user management is done via an external application, but to understand the flow we will do them manually.

-----------------
Create a new user
-----------------

Create 2 new users: one unprivileged and one privileged that will be part of the unprivileged group.

.. code-block:: bash

    # create an user named unprivileged_user
    useradd unprivileged_user

    # check the unprivileged_user, we will see that is part of a group called unprivileged_user
    id unprivileged_user

    # create an user named privileged_user part of the unprivileged_user group
    useradd privileged_user -G unprivileged_user
    
    # check the privileged_user we will see that has 2 groups:
    # primary group: privileged_user
    # secondary group: unprivileged_user
    id privileged_user

Creating 3 new groups, 3 new users, and share access.

.. code-block:: bash

    groupadd --help

    groupadd developers

    groupadd operations

    groupadd devopsgroup

    useradd --help

    useradd dev

    useradd ops

    useradd devops

    usermod --help

    usermod -G developers devops

    usermod -aG operations devops

    id --help

    id devops

+++++++++++++++++++++++++++++++++++++++++
Set a password for the newly created user
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    passwd devops

    passwd --help

    chage -l devops

    chage --help

+++++++++++++++++++++++
Remove users and groups
+++++++++++++++++++++++

When removing users that are part of a group, pay attention.

.. code-block:: bash

    userdel --help

    userdel -r unprivileged_user

    userdel -r privileged_user

    groupdel --help

    groupdel unprivileged_user

    groupdel privileged_user

====
TODO
====

#. create a user named *alice* with UID and GID set to *3001*
#. create a user named *bob* with home directory in */opt*
#. create a user named *john* with comment field set to *John Doe*
#. create a user named *minecraft* with:
    
    - UID *9990*
    - GID *9990*
    - home directory in */usr/games*
    - do not create the home directory
    - no login privileges
#. set a password for alice
#. create a group named *datamanagement* with GID 9001
#. add *alice* and *bob* to the *billing* group
#. configure password aging for *alice* with **chage** command:
    
    -  password validity 31 days
    -  the user should receive warnings 7 days before password expiration
#. lock the *minecraft* account and password 

.. warning::

    Passwords are like underwear. Change them often, don't share them, and don't leave them out for others to see.

