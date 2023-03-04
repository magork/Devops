##########
3. GitHub 
##########

.. note::

    GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that enables developers to automate their software development workflows directly from their GitHub repository.

With GitHub Actions, developers can create custom workflows, called "actions," that automate tasks such as building, testing, and deploying code. These workflows can be triggered by events such as code pushes, pull requests, or scheduled cron jobs.

Some key features of GitHub Actions include:

    #. Automated Workflows: Automating tasks such as building, testing, and deploying code with custom workflows.
    #. GitHub Integration: Triggering workflows from GitHub events, such as code pushes or pull requests, and accessing GitHub data in workflows.
    #. Third-Party Integrations: Integrating with popular tools and services, such as Docker, Kubernetes, AWS, and more.
    #. Container-Based: Running workflows in isolated containers, providing a clean and consistent environment for each job.
    #. Community-Driven: Access to a large library of open-source actions, as well as the ability to share and reuse custom actions within the GitHub community.

GitHub Actions provides a simple and efficient way to automate software development workflows, making it easier to build, test, and deploy code directly from GitHub.

.. code-block:: bash

    # This workflow will install Python dependencies, run tests, and lint with a single version of Python
    name: Python application

    on:
    push:
        branches: [ "main" ]
    pull_request:
        branches: [ "main" ]

    permissions:
    contents: read

    jobs:
    test_python:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3

        - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
            python-version: "3.10"
        
        - name: Install dependencies
        working-directory: source_code/pipelines
        shell: bash
        run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        
        - name: Lint with pylint
        working-directory: source_code/pipelines
        shell: bash
        run: pylint cli/

        - name: Check with mypy
        working-directory: source_code/pipelines
        shell: bash
        run: mypy cli/
        
        - name: Test with pytest
        working-directory: source_code/pipelines
        shell: bash
        run: pytest

A GitHub Actions workflow is composed of a series of events and actions.

    #. Events: Events are triggers that start a workflow, such as a push to the repository, opening a pull request, or scheduling a cron job.

    #. Actions: Actions are individual tasks that make up the workflow, such as checking out code from the repository, building and testing code, or deploying code to a production environment.

A workflow is defined in a YAML file in the .github/workflows directory of a GitHub repository. The structure of a GitHub Actions workflow typically includes:

    #. Name: A unique name for the workflow that identifies it in the GitHub Actions interface.

    #. On: The event that triggers the workflow, such as a push to the repository or opening a pull request.

    #. Jobs: One or more jobs that make up the workflow, each with its own set of steps.

    #. Steps: The individual tasks, or steps, that make up a job. Steps can be individual shell commands or calls to predefined actions from the GitHub Actions marketplace or other sources.

    #. Conditionals: Optional logic that determines whether a step or job should be run, based on conditions such as the success or failure of previous steps or the value of environment variables.

This workflow runs whenever the code is pushed to the main branch of the repository. It consists of one job, "build," that runs on an Ubuntu virtual machine and performs four steps: checking out the code, setting up Node.js, installing dependencies, and building and testing the code.