##################
1. Getting started
##################

=============
Using kubectl
=============

Open Powershell from your Windows machine.

``kubectl`` is the main Kubernetes command-line tool. It's what you'll use for most Kubernetes management tasks, and we use it extensively in the examples. It's available for most operating systems and architectures.

.. code-block:: doscon

    PS C:\Users\xcara> kubectl --help
    kubectl controls the Kubernetes cluster manager.

    Find more information at: https://kubernetes.io/docs/reference/kubectl/

    Basic Commands (Beginner):
    create          Create a resource from a file or from stdin
    expose          Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
    run             Run a particular image on the cluster
    set             Set specific features on objects

    Basic Commands (Intermediate):
    explain         Get documentation for a resource
    get             Display one or many resources
    edit            Edit a resource on the server
    delete          Delete resources by file names, stdin, resources and names, or by resources and label selector

    Deploy Commands:
    rollout         Manage the rollout of a resource
    scale           Set a new size for a deployment, replica set, or replication controller
    autoscale       Auto-scale a deployment, replica set, stateful set, or replication controller

    Cluster Management Commands:
    certificate     Modify certificate resources.
    cluster-info    Display cluster information
    top             Display resource (CPU/memory) usage
    cordon          Mark node as unschedulable
    uncordon        Mark node as schedulable
    drain           Drain node in preparation for maintenance
    taint           Update the taints on one or more nodes

    Troubleshooting and Debugging Commands:
    describe        Show details of a specific resource or group of resources
    logs            Print the logs for a container in a pod
    attach          Attach to a running container
    exec            Execute a command in a container
    port-forward    Forward one or more local ports to a pod
    proxy           Run a proxy to the Kubernetes API server
    cp              Copy files and directories to and from containers
    auth            Inspect authorization
    debug           Create debugging sessions for troubleshooting workloads and nodes

    Advanced Commands:
    diff            Diff the live version against a would-be applied version
    apply           Apply a configuration to a resource by file name or stdin
    patch           Update fields of a resource
    replace         Replace a resource by file name or stdin
    wait            Experimental: Wait for a specific condition on one or many resources
    kustomize       Build a kustomization target from a directory or URL.

    Settings Commands:
    label           Update the labels on a resource
    annotate        Update the annotations on a resource
    completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

    Other Commands:
    alpha           Commands for features in alpha
    api-resources   Print the supported API resources on the server
    api-versions    Print the supported API versions on the server, in the form of "group/version"
    config          Modify kubeconfig files
    plugin          Provides utilities for interacting with plugins
    version         Print the client and server version information

    Usage:
    kubectl [flags] [options]

    Use "kubectl <command> --help" for more information about a given command.
    Use "kubectl options" for a list of global command-line options (applies to all commands).


Verify the cluster with the following command.

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl get nodes
    NAME             STATUS   ROLES           AGE    VERSION
    docker-desktop   Ready    control-plane   6m2s   v1.25.4

The ``kubectl`` configuration file is called config and lives in a hidden directory called ``kube`` in your home directory ``$HOME/.kube/config``. We normally call it the ``kubeconfig`` file, and it contains definitions for

    #. Clusters
    #. Users (credentials)
    #. Contexts

You can view your ``kubeconfig`` using the ``kubectl`` config view command. 

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl config view
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: DATA+OMITTED
        server: https://kubernetes.docker.internal:6443
    name: docker-desktop
    contexts:
    - context:
        cluster: docker-desktop
        user: docker-desktop
    name: docker-desktop
    current-context: docker-desktop
    kind: Config
    preferences: {}
    users:
    - name: docker-desktop
    user:
        client-certificate-data: REDACTED
        client-key-data: REDACTED

You can use ``kubectl`` config current-context to see your current context. The following example shows a system where ``kubectl`` is configured to use the cluster and user-defined in a context called docker-desktop.

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl config current-context
    docker-desktop

Run a ``kubectl`` explain pods command to list all possible Pod attributes.

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl explain pods --recursive
    KIND:     Pod
    VERSION:  v1

    DESCRIPTION:
        Pod is a collection of containers that can run on a host. This resource is
        created by clients and scheduled onto hosts.

    FIELDS:
    apiVersion   <string>
    kind <string>
    metadata     <Object>
        annotations       <map[string]string>
        creationTimestamp <string>
        deletionGracePeriodSeconds        <integer>
        deletionTimestamp <string>
        finalizers        <[]string>
        generateName      <string>
        generation        <integer>
        labels    <map[string]string>
        managedFields     <[]Object>
            apiVersion     <string>
            fieldsType     <string>
            fieldsV1       <map[string]>
            manager        <string>
            operation      <string>
            subresource    <string>
            time   <string>
        name      <string>
        namespace <string>
        ownerReferences   <[]Object>
            apiVersion     <string>
            blockOwnerDeletion     <boolean>
            controller     <boolean>
            kind   <string>
            name   <string>
            uid    <string>
        resourceVersion   <string>
        selfLink  <string>
        uid       <string>
    spec <Object>

To find out more about different attributes, you can use

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl explain pod.metadata
    KIND:     Pod
    VERSION:  v1

    RESOURCE: metadata <Object>

    DESCRIPTION:
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

        ObjectMeta is metadata that all persisted resources must have, which
        includes all objects users must create.

===================
Create a Deployment
===================

.. code-block:: doscon
    
    kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080

    kubectl get deployments
    kubectl get pods
    kubectl get events

================
Create a Service
================

.. code-block:: doscon
    
    kubectl expose deployment hello-node --type=LoadBalancer --port=8080
    kubectl get services

Open ``localhost:8080`` on your browser.

Remove deployment and service.

.. code-block:: doscon

    PS C:\Users\windows_user> kubectl delete service hello-node
    service "hello-node" deleted

    PS C:\Users\windows_user> kubectl delete deployment hello-node
    deployment.apps "hello-node" deleted

