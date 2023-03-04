###############
0. Introduction
###############

.. note::

    Kubernetes is an open-source container orchestration system for automating the deployment, scaling, and management of containerized applications. It is designed to provide a platform-agnostic way to manage and orchestrate containers, whether they are running on-premises or in the cloud.

Kubernetes provides a set of abstractions for defining, deploying, and scaling containerized applications, including:

#. **Pods**: The smallest and simplest unit in the Kubernetes object model, a pod represents a single process or container running in a cluster.
#. **Replication Controllers**: Responsible for ensuring that a specified number of replicas of a pod are running at any given time.
#. **Services**: An abstraction that defines a logical set of pods and a policy by which to access them.
#. **Deployments**: An abstraction that provides declarative updates for Pods and Replication Controllers.
#. Kubernetes also provides a set of built-in features such as **self-healing**, **automatic scaling**, and **rolling updates**, which help to ensure that the applications running on the cluster are always available and up-to-date.

=====================
How Kubernetes works?
=====================

Kubernetes also provides a set of APIs for interacting with the cluster, and it can be easily integrated with a variety of tools and services, such as monitoring, logging, and security.

Kubernetes is widely adopted in the industry for its ability to handle complex, large-scale deployments, it's also a cloud-agnostic, and it can run on most cloud providers as well as on-premises. Its wide adoption also means that there's a large and active community that is constantly working on improving and adding new features to the system.

In summary, Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. It provides a set of abstractions and built-in features for defining, deploying, and scaling containerized applications, as well as a set of APIs for interacting with the cluster. It is widely adopted in the industry for its ability to handle complex, large-scale deployments and its cloud-agnostic nature.

The Kubernetes architecture consists of several components that work together to manage and orchestrate containers in a cluster. The components can be divided into two categories: control plane components and worker node components.

#. Control Plane Components:

    #. API Server: The central component that exposes the Kubernetes API and serves as the control plane for the cluster.
    #. etcd: A distributed key-value store that stores the configuration data for the cluster.
    #. Controller Manager: Manages the various controllers, such as the Replication Controller, that work to maintain the desired state of the cluster.
    #. Scheduler: Assigns Pods to worker nodes based on the resource requirements and constraints defined in the Pod specification.

#. Worker Node Components:

    #. Kubelet: An agent that runs on each worker node, responsible for ensuring that containers are running and healthy.
    #. Container runtime: The software responsible for managing containers on the node, such as Docker or Containerd.
    #. kubeproxy: A network proxy that runs on each worker node and provides network connectivity to Pods.

In addition, Kubernetes also includes several optional components, such as the Kubernetes Dashboard, which provides a graphical interface for managing the cluster, and add-on components, such as ingress controllers, which provide additional functionality for the cluster.

The Kubernetes architecture is designed to be highly scalable, allowing organizations to manage large numbers of containers across multiple worker nodes. The control plane components work together to provide a unified view of the cluster and to ensure that the desired state of the cluster is maintained, while the worker node components provide the computational resources necessary to run containers and Pods.

==========================
Docker Swarm vs Kubernetes
==========================

Docker Swarm and Kubernetes are both container orchestration systems, which means they are used to manage and scale containerized applications. However, there are some key differences between the two:

#. **Architecture**: Docker Swarm is a simple and easy-to-use orchestration system that is built on top of Docker. It uses a single manager node and multiple worker nodes to manage and schedule containers. On the other hand, Kubernetes is a more complex and powerful orchestration system that uses a master-slave architecture, with multiple master and worker nodes that work together to manage and schedule containers.

#. **Scalability**: Kubernetes is designed to handle large-scale deployments and can handle thousands of containers, while Docker Swarm is more limited and is typically used for smaller deployments.

#. **Flexibility**: Kubernetes is more flexible and can run on a variety of platforms, including on-premises, in the cloud, and in hybrid environments. Docker Swarm is more limited and is typically used for deployments in a single environment.

#. **Features**: Kubernetes has a more extensive set of features and built-in capabilities, such as self-healing, automatic scaling, and rolling updates. Docker Swarm has a more limited set of features, but it can be extended through the use of third-party tools.

#. **Community**: Kubernetes has a larger and more active community, with more contributors and a larger number of third-party tools and services available. Docker Swarm has a smaller community, but it is still actively developed and supported.

In summary, Docker Swarm and Kubernetes are both container orchestration systems, but they have some key differences. Kubernetes is more complex and powerful, with a master-

====
Pods
====

A Kubernetes pod is the **smallest and simplest unit** in the Kubernetes object model. It is a group of one or more containers that are deployed together on the same host and share the same network namespace.

A pod provides a **single IP address** and a **single hostname** for all of its containers, allowing them to communicate with each other as if they were on the same host. Pods also share the same storage volumes and can access the same environment variables.

Pods are designed to be ephemeral and disposable, meaning that they can be created and deleted as needed. They are also scalable, as multiple replicas of a pod can be created to handle increased traffic or load.

Pods are the building blocks of Kubernetes applications, and they are used to deploy, scale, and manage the containers that make up an application. They are managed by the Kubernetes controller, which ensures that the desired number of replicas are running and healthy at all times.

Overall, Pods are the basic and important unit of deployment in Kubernetes, and they allow you to run one or more containers in a defined and manageable way.

.. note::

    Guidelines issued by the Inclusive Naming Initiative (inclusivenaming.org) promote responsible language and tries to avoid harmful terms.

    https://inclusivenaming.org/word-lists/tier-1/