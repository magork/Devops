###############
0. Introduction
###############

============
What is GIT?
============

Git is a distributed version control system. This means that a local clone of the project is a complete version control repository. These fully-functional local repositories make it easy to work offline or remotely. Developers commit their work locally, and then sync their copy of the repository with the copy on the server. This paradigm differs from centralized version control where clients must synchronize code with a server before creating new versions of code.

Every time work is saved, Git creates a **commit**. A commit is a snapshot of all files at a point in time. If a file has not changed from one commit to the next, Git uses the previously stored file.

**Branches**, which are lightweight pointers to work in progress, manage this separation. Once work created in a branch is finished, it can be merged back into the team's main (or trunk) branch.

=================
Connect to GitHub
=================

There are 2 ways to log in to GitHub:

* keys

* credentials (username and password)

Generate the key from your local machine and upload it to GitHub

.. code-block:: bash

  # In a DevOps environment we want to have as much information as possible
  ssh-keygen -t ed25519 -C "user@hostname"

========================
What exactly is ed25519?
========================

ed25519 is a new cryptography solution that provides the Edwards-curve Digital Signature Algorithm (EdDSA).

Similarly, not all software solutions currently support ed25519, but SSH implementations in most modern operating systems do.

Why is ed25519 Key a Good Idea?

When compared to the most common type of SSH key - RSA - ed25519 offers several interesting advantages:

    #. It is faster to generate and verify

    #. it is more secure collision resilience - that is, it is more resistant to hash-function collision attacks (types of attacks where large numbers of keys are generated with the hope of getting two different keys to have matching hashes)

    #. The keys are smaller, which means they are easier to transfer and copy/paste.

Read the newly generated key

.. code-block:: bash

    cat ~/.ssh/id_ed25519.pub

    # Upload the newly generated key to GitHub
    # https://github.com/settings/keys

    # Clone projects on your local machine

We will learn how to use the terminal, console version of git, how to use vim, and fix merge conflicts.

.. code-block:: bash
  
    # install git
    sudo apt install git

    # verify that git is installed
    git --version

    # change directory to home
    cd ~

    # creates a directory
    mkdir sandbox 
    cd sandbox
    
    # download the project

    git clone git@github.com:SKILLAB-DevOps/git.git 
    cd git # change directory to project
    git branch -a # check what branches are available
    git checkout master # move to a different branch
    git checkout develop # move back to develop  
    git checkout -b feature/yourName # create a new branch with your name

===========================
1. Create a scripts project
===========================

Create a new project in your userspace named ``scripts``. Press on the Kitten on the top left then new.

.. code-block:: bash

    # Clone the new project
    git clone git@github.com:<USER>/scripts.git

    # Change the directory to your new repository
    cd scripts
 
    # Config GitHub information
    git config --global user.email "MAIL"
    git config --global user.name "<USER>"

    # Create a new script
    vim HelloWorld

    # Add Hello World in it
    # Check the files that will be pushed to remote
    git status
    
    # Add the HelloWorld in git staging
    git add HelloWorld

    # Add a commit message
    git commit -m "Initial commit"

    # Push the code
    git push

===================================================
2. Add your presentation into Skillab - git project
===================================================

Create a markdown file with your name and some information use at least 5 different syntaxes from https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

I have added an example, but be creative:

.. code-block:: bash

    **Claudiu**
    *DevOps Engineer*
    Likes:

      * [x] coding
      * [x] teaching
      * [x] video games
      * [x] mma

I would like to have in the presentation:

    #. name
    #. profession
    #. hobbies
    #. why are you here?
    #. do you like DevOps?
    #. what would you like more?
    #. what would you like less

======
How to
======

.. code-block:: bash

    vim presentations.md # keep this name so we can have some merge conflicts

    git add presentations.md
    # or
    # pay attention it adds everything

    git add --all

    # now press the letter "i" to insert
    # when you are done writing press the ESCAPE key

    # write :wq and press ENTER

    git commit -m "Message" # Keep message informative

    git push

=======================
Solving merge conflicts
=======================

To resolve a Git merge conflict, follow these steps:

    #. Identify the conflicting file(s): Git will mark the conflicts in the affected files with conflict markers.
    #. Open the conflicting file(s) and locate the conflict markers.
    #. Choose which version to keep or manually edit the file to include the changes you want.
    #. Remove the conflict markers (e.g. "<<<<<<<").
    #. Commit the resolved file(s).
    #. Repeat the process for any other conflicting files.

It's important to carefully review the changes and make sure the resulting file is what you intended before committing. You may also want to consider using a merge tool to assist with resolving conflicts.
