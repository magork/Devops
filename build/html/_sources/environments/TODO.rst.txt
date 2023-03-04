#######
4. TODO
#######
=========
Questions
=========

1. What is not a cloud computing service?

    #. **Infrastructure as a Service (IaaS)** IaaS is a pay-as-you-go cloud computing service that offers on-demand storage and networking resources.
    #. **Software as a Service (SaaS)** This service allows clients and customers to connect with cloud-based apps that provide email, teleconferencing, productivity, and storage services.
    #. **Code as a Service** CODEaaS offers you complete, no-to-low code integration with your software.
    #. **Platform as a Service (PaaS)** PaaS offers complete cloud-based development and deployment where a client can create simple or the most sophisticated cloud-based applications.
    #. **Serverless** Serverless cloud computing is an architecture where the service provider manages the execution of the code instead of deploying them on servers.”*

2. What is not a model of deployment in the cloud?

    #. Private Cloud
    #. Public Cloud
    #. Deep Web/Dark Cloud
    #. Community Cloud
    #. Hybrid Cloud

3. What is not an advantage of cloud computing?

    #. accessibility
    #. cost-effective
    #. security
    #. performance
    #. flexibility
    #. scalability
    #. usability

======
Task 1
======

Open your container using ``docker run -it fedora bash`` then:

    #. store tree output for the 2nd level of root ``tree -d -L 2 /`` output in a hidden file on your sandbox directory in home explicitly ``.output``
    #. append to the ``.output`` the output from ``/var/log/dnf.log``
    #. count total words and how many times DEBUG is present from the ``.output``
    #. clear the content of the ``.output`` file
    #. execute command ``rm -rf /*``
