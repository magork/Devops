##########
2. Jenkins
##########

.. note::

    Jenkins is a popular open-source automation server for building, testing, and deploying software. It provides a way to automate the software development process, including building, testing, and deploying code, enabling developers to focus on writing code.

Jenkins supports a wide range of development languages, platforms, and tools and can be extended through the use of plugins. It can be run on-premises or in the cloud, and can be easily integrated with other tools and services, such as Git, Docker, and Kubernetes.

Some key features of Jenkins include:

    #. Continuous Integration: Automatically building and testing code every time changes are committed to a code repository.
    #. Pipeline Support: Creating and executing pipelines, a series of tasks and stages, to automate the software development process.
    #. Plugins: Extending Jenkins functionality through the use of plugins, which add new features and capabilities to Jenkins.
    #. Distributed Builds: Running builds on multiple machines in parallel to improve build times and reduce the risk of build failures.
    #. Reporting and Monitoring: Providing real-time feedback and notifications on build results, including test results and code quality metrics.

Jenkins is widely used for continuous integration and delivery and provides a flexible and scalable platform for automating the software development process.

.. code-block:: bash

    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11