########################
2. Creating a Deployment
########################

.. note::

    A Kubernetes Deployment is a declarative way to manage the desired state of a group of containers. A Deployment defines the desired state of your application, including the number of replicas you want to run and the configuration of the containers.

The Deployment ensures that the desired state is always maintained, even if worker nodes in the cluster fail. If a node fails, the Deployment automatically replaces the containers running on that node with new containers on another node.

A Deployment also provides other benefits, such as rolling updates and rollbacks. A rolling update allows you to update your application without downtime, by gradually replacing old replicas with new ones. If there is an issue with the update, you can easily roll back to the previous version of your application.

To create a Deployment, you need to provide a YAML file that defines the desired state of your application, including the number of replicas, the image for the containers, and the desired state of the containers. You can then use the Kubernetes command line interface (CLI) to create the Deployment.

A Kubernetes Deployment is a powerful tool that provides a simple and reliable way to manage the desired state of your applications in a cluster, allowing you to easily scale, update, and manage your applications. 

Create a new file ``nginx-deployment.yaml``

.. code-block:: bash

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: nginx-deployment
    labels:
        app: nginx
    spec:
    replicas: 3
    selector:
        matchLabels:
        app: nginx
    template:
        metadata:
        labels:
            app: nginx
        spec:
        containers:
        - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80

.. code-block:: bash

    kubectl apply -f nginx-deployment.yaml

.. code-block:: bash

    linux_user@linux_machine:~/sandbox $ kubectl get deployments
    NAME               READY   UP-TO-DATE   AVAILABLE   AGE
    nginx-deployment   3/3     3            3           4m14s

Find out more:
.. code-block:: bash

    kubectl describe deployments

Updating running deployments

.. code-block:: bash

    kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
    # or 
    kubectl edit deployment/nginx-deployment

    # Roll the update
    kubectl rollout status deployment/nginx-deployment