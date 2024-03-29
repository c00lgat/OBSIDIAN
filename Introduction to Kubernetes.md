qhttps://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home

**Welcome to LFS158x - Introduction to Kubernetes!**

We strongly recommend that you review the course syllabus before jumping into the content. It provides the most important information related to the course, including:

- Course overview
- Instructors biographies and targeted audience
- Course prerequisites and length
- Course learning objectives and the outline
- edX platform guidelines
- Discussion forums, course timing, and learning aids
- Grading, progress, and course completion
- Audit and verified tracks
- The Linux Foundation's history, events, training, and certifications.
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@LFS158x_Course_Syllabus__2022_.pdf]]

**Course Learning Objectives**
By the end of this course, you should be able to:
- Understand the origin, architecture, primary components and building blocks of Kubernetes.
- Set up and access a Kubernetes cluster using Minikube.
-  Run applications on the deployed Kubernetes environment, and access the deployed applications.
-  Understand the usefulness of Kubernetes communities, and how you can participate.
---
# Chapter 1. From Monolith to Microservices

By the end of this chapter, you should be able to:
- Explain what a monolith is.
- Discuss the monolith's challenges in the cloud.
- Explain the concept of microservices.
- Discuss microservices advantages in the cloud.
- Describe the transformation path from a monolith to microservices.

A Monolith software is extremely pricey to maintain. It has to run on a single system that is not only pricey but also complex and at times, challenging to procure. 

Since the Monolith application runs as a single process, the scaling of individual features is almost impossible. 
Although scaling can be achieved manually through deployment of the application on another server, typically behind a load balancer - another pricey option.

Monolith application down time during updates, upgrades, patches or migrations is inevitable. Maintenance windows have to be planned well in advance.

### The Modern Microservice
An analogy of pebbles, and a 1000-ton boulder has been mentioned to try and demonstrate how the two approaches work and how efficient they are. 
The pebbles are the microservices of which the application is made out of.
But on the other hand, with the Monolith approach, the 1000-ton boulder represents the single process-single system application that is extremely hard to maintain, change, upgrade, update and scale.

While the pebbles, when weighed up, will weigh as much as the boulder, it is still much easier to pick up smaller pebbles and do whatever is needed and only then add them up to the pebble bucket. 

The pebbles are easy to select and grouped together based on color, size, shape and require minimal effort to relocate when needed. 

Relocating a 1000-ton boulder on the other hand is, well, not so easy.

**Microservices** can be deployed individually on separate servers provisioned with fewer resources - only what is required by each service and the host system itself, helping to lower compute resource expenses.

Microservices-based architecture is aligned with Event-driven Architecture and Service-Oriented Architecture (SOA) principles. 

> *Event-driven Architecture* uses events to trigger and communicate between decoupled services and is common in modern applications built with microservices. An event is a change in state, or an update, like an item being placed in a shopping cart on an e-commerce website. Events can either carry the state (the item purchased, its price, and a delivery address) or events can be identifiers (a notification that an order was shipped). 

>Event-driven architectures have *three* key components: event producers, event routers, and event consumers. A producer publishes an event to the router, which filters and pushes the events to consumers. Producer services and consumer services are decoupled, which allows them to be scaled, updated, and deployed independently.

Below is a demonstration of an Event-driven architecture (Taken from AWS).
![[1-SEO-Diagram_Event-Driven-Architecture_Diagram.b3fbc18f8cd65e3af3ccb4845dce735b0b9e2c54.png]]

>*Service-Oriented Architecture (SOA) Principles*:There are 9 types of SOA design principles. 
- Standardized Service Contract (Services adhere to a service description)
- Loose Coupling (Less dependency on each other)
- Service Abstraction (Services hide the logic they encapsulate from the outside world)
- Service Reusability (Logic is divided into services with the intent of maximizing reuse)
- Service Autonomy (Services should have control over the logic they encapsulate)
- Service Statelessness (This means that services should not withhold information from one state to the other)
- Service Discoverability (Services can be discovered (usually in a service registry))
- Service Composability (Services break big problems into little problems)
- Service Interoperability (Services should use standards that allow diverse subscribers to use the service)
https://www.guru99.com/soa-principles.html

Microservices are made out of smaller independent processes which communicate with each other through APIs over a network. 
APIs allow internal and external access to the services.

Although Microservices do add up to the complexity of a system, their distributed nature allows for easy scalability, which is one of it's biggest benefits.
Since Microservices allow modularity, each component or each microservice can be scaled individually, either manually, or automatically through demand-based autoscaling. 

As opposed to Monolith Architecture, Microservices allow for virtually no downtime and no service disruption to clients while updating, upgrading or going through changes as they are usually rolled out seamlessly.

Thus, Microservices allow for an agile approach of development, having separate teams focus on separate features, thus making development more efficient and productive.

### Refactoring
Some Monolith applications are harder than others in migrating to a Microservices approach. Some have failed, even.

There exists two approaches to breaking down a Monolith application into a Microservices based application:
- "Bang-bang" approach: focuses all efforts on refactoring of the Monolith, postponing the development and implementation of any new features - essentially delaying progress.
- An incremental refactoring approach: new features are developed and implemented as modern microservices which are able to communicate with the Monolith through APIs with no dependency on the Monolith's code. Existing features within the Monolith are also slowly being refactored out and being modernized and the Monolith starts slowly fading away. Gradual transition, allows for phased migration of the application features.

If an enterprise chooses to go through the Incremental refactoring approach, a Roadmap is needed to highlight the development timeline and order of features to separate from the Monolith and turn into distributed Microservices, how to decouple dependent components such as the databases from the application to separate data complexity from application logic and more. 

Through refactoring, a Monolith receives a second chance at life. To live on as a modular system adapted to fully integrate with today's fast-paced cloud automation tools and services.

### Challenges
Not all Monoliths are able to be turned into Microservice based applications. Some even fail. 
There are multiple considerations to take before one proceeds to modernize a Monolith application.

**Poor candidates**
If a Monolith application is written in legacy code such as Cobol or Assembly, it might make more sense to just rebuild it from the ground up as a cloud-native application. 

A poorly designed legacy application should be re-designed and re-built from scratch using modern architectural patterns for microservices and even containers.

Applications tightly coupled with data stores are also poor candidates for refactoring.

**Post Refactoring Challenges**
Once a Monolith survives the refactoring phase, the next challenge is to design mechanisms or find suitable tools to keep the decoupled modules alive and ensure the application resiliency as a whole.

**Runtimes**
Choosing runtimes might pose another challenge. Running many modules on a single physical or virtual server could result in libraries conflicting with each other; causing errors and failures. 
This forces running each individual module on its own server where such conflicts could be eliminated but that is not an economical way of resource management. 
That also results in wasting server resources as each server has the same main dependencies and libraries such as the Operating System.
At times, the OS consumes more resources than the Modules themselves.

**Solution**
Application Containers. 
They provide encapsulated lightweight runtime environment for application modules. 

Consistent software environments for developers, testers, all the way from development to production.

Containers ensure application portability from physical bare-metal  to Virtual Machines, but this time, with multiple applications deployed on the very same server, each running in their own execution environments isolated from each other, avoiding conflicts, errors and failures.

Other features include higher server utilization, individual module scalability, flexibility, interoperability and easy integration with automation tools.

###### Learning Objectives:
You should now be able to:
- Explain what a monolith is.
- Discuss the monolith's challenges in the cloud.
- Explain the concept of microservices.
- Discuss microservices advantages in the cloud.
- Describe the transformation path from a monolith to microservices.

---
# Chapter 2. Container Orchestration

## Introduction
Container images allow us to confine the application code, along with its dependencies and runtime in a pre-defined format.

Container runtimes such as *runC*, *containerd* and *cri-o* can use pre-packaged images as a source to create and run one or more containers.

While these runtimes can run multiple containers on a single host, in practice, we would like to have a fault-tolerant and scalable solution. 
Such solution is achieved by building a single **controller/management unit**, a collection of multiple hosts connected together.
This controller/management unit is generally referred to as a ***container orchestrator***.


**Learning Objectives**
By the end of this chapter, you should be able to:
- Define the concept of container orchestration.
- Explain the benefits of using container orchestration.
- Discuss different container orchestration options.
- Discuss different container orchestration deployment options.

## What Are Containers?
Containers allow us to deploy Microservice based application on any infrastructure of our choice. It provides a high-performing, scalable solution as opposed to the Monolith approach. 
Containers are best suited to deliver microservices by providing portable, isolated virtual environments for applications to run without interference from other running apps.

![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@Container_Deployment.png]]
Container deployment.

Microservices are lightweight applications written in various modern programming languages with specific dependencies, libraries and environmental requirements.
To ensure an application has everything it needs in order to run, it is packaged together with its dependencies.

Containers encapsulate microservices but do not run them directly. Containers run container images.

A *Container Image* bundles the application along with its runtime, libraries and dependencies and is the source of a container deployed to offer an isolated executable environment for the application.
They can be deployed using any specific container image and on many different platforms such as servers, virtual servers, public cloud, etc.

## What Is Container Orchestration?
Running containers in Development on a single host is usually fine but, in environments such as QA and Production, that is no longer a viable option as containers need to meet more specific demands: 
- Fault-tolerance
- On-demand scalability
- Optimal resource usage
- Auto-discovery to automatically discover and communicate with each other
- Accessibility from the outside world
- Seamless updates/rollbacks without any downtime

**Container Orchestration** are tools which group systems together to form clusters where containers' deployment and management is automated at scale while meeting the requirements mentioned above.


## Container Orchestrators
- [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)  
    Amazon Elastic Container Service (ECS) is a hosted service provided by [Amazon Web Services](https://aws.amazon.com/) (AWS) to run containers at scale on its infrastructure.
-  [Azure Container Instances](https://azure.microsoft.com/en-us/products/container-instances/#overview)  
    Azure Container Instance (ACI) is a basic container orchestration service provided by [Microsoft Azure](https://azure.microsoft.com/en-us/).
-  [Azure Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/)  
     Azure Service Fabric is an open source container orchestrator provided by [Microsoft Azure](https://azure.microsoft.com/en-us/).
-  [Kubernetes](https://kubernetes.io/)  
    Kubernetes is an open source orchestration tool, originally started by Google, today part of the [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) project.
-  [Marathon](https://mesosphere.github.io/marathon/)  
    Marathon is a framework to run containers at scale on [Apache Mesos](https://mesos.apache.org/) and [DC/OS](https://dcos.io/).
-  [Nomad](https://www.nomadproject.io/)  
     Nomad is the container and workload orchestrator provided by [HashiCorp](https://www.hashicorp.com/).
-  [Docker Swarm](https://docs.docker.com/engine/swarm/)  
	Docker Swarm is a container orchestrator provided by [Docker, Inc](https://www.docker.com/). It is part of [Docker Engine](https://docs.docker.com/engine/).

Container orchestrators are also explored in another edX MOOC, [_"Introduction to Cloud Infrastructure Technologies"_](https://www.edx.org/course/introduction-to-cloud-infrastructure-technologies) (LFS151x). We highly recommend that you take this course.

## Why Use Container Orchestrators?
While manually maintaining a couple of containers or dozens of them, orchestrators make things much easier for users especially when it comes to managing hundreds or thousands of containers running on a global infrastructure.

*Most container orchestrators can:*
- Group hosts together while creating a cluster.
- Schedule containers to run on hosts in the cluster based on resources availability.
- Enable containers in a cluster to communicate with each other regardless of the host they are deployed to in the cluster.
- Bind containers and storage resources.
- Group sets of similar containers and bind them to load-balancing constructs to simplify access to containerized applications by creating an interface, a level of abstraction between the containers and the client.
- Manage and optimize resource usage.
- Allow for implementation of policies to secure access to applications running inside containers.

## Where to Deploy Container Orchestrators?
On bare metal, Virtual Machines, on-premises, on public and hybrid clouds. Kubernetes, for example, can be deployed on a workstation, with or without an isolation layer such as a local hypervisor or container runtime, inside a company's data center, in the cloud on AWS Elastic Compute Cloud (EC2) instances, Google Compute Engine (GCE) VMs, DigitalOcean Droplets, OpenStack, etc.

Last but not least, there is the managed container orchestration as-a-Service, more specifically the managed Kubernetes as-a-Service solution, offered and hosted by the major cloud providers, such as [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service/#overview) (AKS), [DigitalOcean Kubernetes](https://www.digitalocean.com/products/kubernetes), [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) (GKE), [IBM Cloud Kubernetes Service](https://www.ibm.com/cloud/kubernetes-service), [Oracle Container Engine for Kubernetes](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/), or [VMware Tanzu Kubernetes Grid](https://tanzu.vmware.com/kubernetes-grid).

**Learning Objectives (Review)**
You should now be able to:
- Define the concept of container orchestration.
- Explain the benefits of using container orchestration.
- Discuss different container orchestration options.
- Discuss different container orchestration deployment options.

---
# Chapter 3. Kubernetes

## Introduction
**Chapter Overview**
In this chapter, we describe Kubernetes, its features, and the reasons why you should use it. We will explore the evolution of Kubernetes from Borg, Google's very own distributed workload manager.

We will also learn about the Cloud Native Computing Foundation (CNCF), which currently hosts the Kubernetes project, along with other popular cloud-native projects, such as Prometheus, Fluentd, cri-o, containerd, Helm, Envoy, and Contour, just to name a few.

**Learning Objectives**
By the end of this chapter, you should be able to:
- Define Kubernetes.
- Explain the reasons for using Kubernetes.
- Discuss the features of Kubernetes.
- Discuss the evolution of Kubernetes from Borg.
- Explain the role of the Cloud Native Computing Foundation.

## What Is Kubernetes?
According to the [Kubernetes website](https://kubernetes.io/),
_"Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications"._

Kubernetes comes from a Greek word, which means *helmsman* or *ship pilot*. We can think of Kubernetes as the pilot on a ship of containers.

Kubernetes is also referred to as **k8s** (pronounced Kate's), as there are 8 characters between k and s.

Kubernetes is highly inspired by the Google Borg system, a container and workload orchestrator for its global operations for more than a decade. It is an open source project written in the Go language and licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Kubernetes was started by Google and, with its v1.0 release in July 2015, Google donated it to the [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF), one of the largest sub-foundations of the [Linux Foundation](https://www.linuxfoundation.org/).

## From Borg to Kubernetes
According to the abstract of Google's [Borg paper](https://research.google/pubs/pub43438/), published in 2015,
_"Google's Borg system is a cluster manager that runs hundreds of thousands of jobs, from many thousands of different applications, across a number of clusters each with up to tens of thousands of machines"._

For more than a decade, Borg has been Google's secret, running its worldwide containerized workloads in production. Services we use from Google, such as Gmail, Drive, Maps, Docs, etc., are all serviced using Borg. 

Among the initial authors of Kubernetes were Google employees who have used Borg and developed it in the past. They poured in their valuable knowledge and experience while designing Kubernetes. Several features/objects of Kubernetes that can be traced back to Borg, or to lessons learned from it, are:
- API servers
- Pods
- IP-per-Pod
- Services
- Labels.

## Kubernetes Features
Kubernetes offers a very rich set of features for container orchestration. Some of its fully supported features are:
- **Automatic bin packing**  
    Kubernetes automatically schedules containers based on resource needs and constraints, to maximize utilization without sacrificing availability.
- **Designed for extensibility**  
    A Kubernetes cluster can be extended with new custom features without modifying the upstream source code.
- **Self-healing**  
    Kubernetes automatically replaces and reschedules containers from failed nodes. It terminates and then restarts containers that become unresponsive to health checks, based on existing rules/policy. It also prevents traffic from being routed to unresponsive containers.
- **Horizontal scaling**  
    With Kubernetes applications are scaled manually or automatically based on CPU or custom metrics utilization.
- **Service discovery and load balancing**  
    Containers receive IP addresses from Kubernetes, while it assigns a single Domain Name System (DNS) name to a set of containers to aid in load-balancing requests across the containers of the set.

Additional fully supported Kubernetes features are:
- **Automated rollouts and rollbacks**  
    Kubernetes seamlessly rolls out and rolls back application updates and configuration changes, constantly monitoring the application's health to prevent any downtime.
- **Secret and configuration management**  
    Kubernetes manages sensitive data and configuration details for an application separately from the container image, in order to avoid a rebuild of the respective image. Secrets consist of sensitive/confidential information passed to the application without revealing the sensitive content to the stack configuration, like on GitHub.
- **Storage orchestration**  
    Kubernetes automatically mounts software-defined storage (SDS) solutions to containers from local storage, external cloud providers, distributed storage, or network storage systems.
- **Batch execution**  
    Kubernetes supports batch execution, long-running jobs, and replaces failed containers.
- **IPv4/IPv6 dual-stack**  
    Kubernetes supports both IPv4 and IPv6 addresses.


## Why Use Kubernetes?
Portability. Can be used in many environments such as local or remote VMs, bare metal, or in public/hybrid/private/multi-cloud setups.

Kubernetes' architecture is modular. It allows third party open source tools to support it which enhances the user experience and allows for a wider set of features. 
In addition to orchestrating modular, decoupled microservices type application, but also its architecture follows decoupled microservices patterns. 
Functionality can be extended by writing custom resources, operators, custom APIs, scheduling rules or plugins.

Has a wide thriving community to support it across the globe. The community is called *Kubernetes Community*.

## Cloud Native Computing Foundation (CNCF)

![[cncf-color-bg.png]]

The [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) is one of the largest sub-projects hosted by the [Linux Foundation](https://www.linuxfoundation.org/). CNCF aims to accelerate the adoption of containers, microservices, and cloud-native applications.

CNCF hosts a multitude of projects, with more to be added in the future. CNCF provides resources to each of the projects, but, at the same time, each project continues to operate independently under its pre-existing governance structure and with its existing maintainers. Projects within CNCF are categorized based on their maturity levels: Sandbox, Incubating, and Graduated. At the time of this writing, over a dozen projects had reached Graduated status with many more Incubating and in the Sandbox.

*Popular graduated projects*:
- [Kubernetes](https://kubernetes.io/) container orchestrator
- [etcd](https://etcd.io/) distributed key-value store
- [CoreDNS](https://coredns.io/) DNS server
- [containerd](http://containerd.io/) container runtime
- [Envoy](https://www.envoyproxy.io) cloud native proxy
- [Fluentd](http://www.fluentd.org/) for unified logging
- [Harbor](https://goharbor.io/) registry
- [Helm](https://www.helm.sh/) package management for Kubernetes
- [Linkerd](https://linkerd.io/) service mesh for Kubernetes
- [Open Policy Agent](https://www.openpolicyagent.org/) policy engine
- [Prometheus](https://prometheus.io/) monitoring system and time series DB
- [Rook](https://rook.io/) cloud native storage orchestrator for Kubernetes

*Key incubating projects*:
- [argo](https://argoproj.github.io/) workflow engine for Kubernetes
- [Buildpacks.io](https://buildpacks.io/) builds application images
- [CRI-O](https://cri-o.io) container runtime
- [Contour](https://projectcontour.io/) ingress controller for Kubernetes
- [gRPC](http://www.grpc.io/) for remote procedure call (RPC)
- [CNI](https://www.cni.dev/) for Linux containers networking
- [flux](https://fluxcd.io/) continuous delivery for Kubernetes
- [Knative](https://knative.dev/) serverless containers in Kubernetes
- [KubeVirt](https://kubevirt.io/) Kubernetes based Virtual Machine manager
- [Notary](https://github.com/theupdateframework/notary) for data security
- And many [more](https://www.cncf.io/projects/).

There are many dynamic projects in the CNCF [Sandbox](https://www.cncf.io/sandbox-projects/) geared towards metrics, monitoring, identity, scripting, serverless, nodeless, edge, expecting to achieve Incubating and possibly Graduated status. While many active projects are preparing for takeoff, others are being [archived](https://www.cncf.io/archived-projects/) once they become less active and no longer in demand. The first projects to be archived are the [rkt](https://github.com/rkt/rkt) container runtime, the distributed [OpenTracing](https://www.cncf.io/projects/opentracing/), and [Brigade](https://brigade.sh/), an event driven automation tool.

The projects under CNCF cover the entire lifecycle of a cloud-native application, from its execution using container runtimes, to its monitoring and logging. This is very important to meet the goals of CNCF.

## CNCF and Kubernetes
For Kubernetes, the Cloud Native Computing Foundation:
- Provides a neutral home for the Kubernetes trademark and enforces proper usage.
- Provides license scanning of core and vendor code.
- Offers legal guidance on patent and copyright issues.
- Creates and maintains open source learning [curriculum](https://github.com/cncf/curriculum), [training](https://www.cncf.io/certification/training/), and certification for Kubernetes and [cloud native associates](https://www.cncf.io/certification/kcna/) (KCNA), [administrators](https://www.cncf.io/certification/CKA/) (CKA), [application developers](https://www.cncf.io/certification/ckad/) (CKAD), and [security specialists](https://www.cncf.io/certification/cks/) (CKS).
- Manages a software conformance [working group](https://lists.cncf.io/g/cncf-k8s-conformance).
- Actively markets Kubernetes.
- Supports ad hoc activities.
- Sponsors conferences and meetup events.

---
# Chapter 4. Kubernetes Architecture
## Introduction
In this chapter, we will explore the **Kubernetes architecture**, the components of a **control plane node**, the role of the **worker nodes**, the cluster state management with **etcd** and the network setup requirements. We will also learn about the **Container Network Interface (CNI)**, as Kubernetes' network specification.

**Learning Objectives**
By the end of this chapter, you should be able to:
- Discuss the Kubernetes architecture.
- Explain the different components of the control plane and worker nodes.
- Discuss cluster state management with etcd.
- Review the Kubernetes network setup requirements.

## Kubernetes Architecture
At a very high level, Kubernetes is a cluster of compute systems categorized by their distinct roles:
- One or more **control plane** nodes
- One or more **worker** nodes (optional, but recommended).

![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@TrainingImage.png]]

### **Control Plane Node overview**
The Control Plane Node is the brain behind all operations inside the cluster. 
It is an environment that encapsulates *control plane agents* that are responsible for managing the state of a Kubernetes cluster.
The *control plane agents* have very distinct roles in the cluster's management.

The Kubernetes cluster can be communicated with by the user via the CLI, Web UI and an API.

The Control Plane is <mark style="background: #FFB86CA6;">very crucial</mark>. Losing it means <mark style="background: #FF5582A6;">downtime</mark>. Causing service disruption to clients, with possible loss of business.
To ensure durability and reliability, control plane node replicas can be added to the cluster, configured in High-Availability (HA) mode.

Only one Control Plane node is active in managing the cluster once at a time, the control plane components stay in sync across the control plane node replicas. 
This type of configuration adds resiliency to the clusters control plane, should the active control plane node fail.

To persist the Kubernetes' cluster state, all cluster configuration is saved to a distributed key-value store which only holds cluster state related data.
The key-value store may be configured on the control plane node ([[Stacked Topology Kubernetes]]), or on its dedicated host ([[External Topology Kubernetes]]) to help reduce the chances of data store loss by decoupling it from the other control plane agents.

In the stacked key-value store topology, HA control plane node replicas ensure the key-value store's resiliency as well. However, that is not the case with external key-value store topology, where the dedicated key-value store hosts have to be separately replicated for HA, a configuration that introduces the need for additional hardware, hence additional operational costs.

## **Control Plane Node Components**
https://kubernetes.io/docs/concepts/overview/components/
A control plane node runs the following essential control plane components and agents:
- API Server
- Scheduler
- Controller Managers
- Key-Value Data Store.

In addition, the control plane node runs:
- Container Runtime
- Node Agent
- Proxy
- Optional add-ons for cluster-level monitoring and logging.

### **Control Plane Node Components: API Server**
https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/

The [[kube-apiserver]] is a crucial component that runs in the *Control Plane Node*.

<mark style="background: #FFF3A3A6;">Analogy:</mark> API Server is like the secretary. It receives the calls from all surrounding parties, checks the state of the company (cluster), updates it accordingly after the calls are approved in the calendar (state store). The secretary is the only person to read the calendar and make changes and save them. The secretary is the person for when any other company wants to inquire about the company's state. 

The API Server intercepts RESTful calls from users, administrators, developers, operators and external agents. It validates and processes the API calls.

During processing, the API Server reads the Kubernetes cluster's current state from the key-value store, and after a call's execution, the resulting state of the Kubernetes cluster is saved in the key-value store for persistence.

Meaning, changes are saved in the key-value store for persistence. 

The API Server is the only control plane component to talk to the key-value store, both to read from and to save Kubernetes cluster state information, acting as a middle interface for any other control plane agent inquiring about the cluster's state.

The API Server is very configurable and customizable. It can scale horizontally, and supports the addition of custom secondary API Servers, a config that transforms the primary API Server int o a proxy to all secondary, custom API Servers, routing all incoming RESTful calls to them based on customer defined rules (Load Balancer?).

### **Control Plane Node Components: Scheduler**
https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/

https://kubernetes.io/docs/concepts/scheduling-eviction/

The role of the *kube-scheduler* is to assign new workload objects, such as pods encapsulating container, to nodes - typically worker nodes. 
During the scheduling process, decisions are made based on current Kubernetes cluster state and new workload object's requirements.

The *kube-scheduler* obtains the resources usage data for each worker node in the cluster from the key-value store via the API Server.

The *kube-scheduler* also receives the new workload object's requirements which are part of its configuration data (of the workload object). It receives it from the API Server as well.

Requirements may include constraints that users and operators set. Such as scheduling work on a node labeled with **disk=\=ssd**  key-value pair.

The *kube-scheduler* also takes into account Quality of Service (QoS) requirements, data locality, affinity, anti-affinity, taints, toleration, cluster topology, etc.

Once all the cluster data is available, the scheduling algorithm filters the nodes with predicates to isolate the possible node candidates which then are scored with priorities in order to select the one node that satisfies all the requirements for hosting the new workload. The outcome of the decision process is communicated back to the API Server, which then delegates the workload deployment with other control plane agents.

The Scheduler is highly configurable and customizable through scheduling policies, plugins, and profiles.
Additional custom schedulers are also supported, then the object's configuration data should include the name of the custom scheduler expected to make the scheduling decision for that particular object; if no such data is included, the default scheduler is selected instead.

A scheduler is extremely important and complex in a multi-node Kubernetes cluster, while in a single-node Kubernetes cluster possibly used for learning and development purposes, the scheduler's job is quite simple.

### **Control Plane Node Components: Controller Managers**
The **controller managers** are components of the control plane node running controllers or operator processes to regulate the state of the Kubernetes cluster. Controllers are watch-loop processes continuously running and comparing the cluster's desired state (provided by objects' configuration data) with its current state (obtained from the key-value store via the API Server). In case of a mismatch, corrective action is taken in the cluster until its current state matches the desired state.

The **kube-controller-manager** runs controllers or operators responsible to act when nodes become unavailable, to ensure container pod counts are as expected, to create endpoints, service accounts, and API access tokens.

The **cloud-controller-manager** runs controllers or operators responsible to interact with the underlying infrastructure of a cloud provider when nodes become unavailable, to manage storage volumes when provided by a cloud service, and to manage load balancing and routing.

### **Control Plane Node Components: Key-Value Data Store**

https://etcd.io/docs/v3.5/

[**etcd**](https://etcd.io) is an open source project under the [Cloud Native Computing Foundation](https://www.cncf.io) (CNCF). etcd is a strongly consistent, distributed **key-value data store** used to persist a Kubernetes cluster's state. New data is written to the data store only by appending to it, data is never replaced in the data store. Obsolete data is compacted (or shredded) periodically to minimize the size of the data store.

Out of all of the Control Plane components, <mark style="background: #BBFABBA6;">only the API Server</mark> is able to communicate with the etcd data store.

etcd's CLI management tool - **etcdctl**, provides snapshot save and restore capabilities which come in handy especially for a single etcd instance Kubernetes cluster - common in Development and learning environments. However, in Stage and Production environments, it is extremely important to replicate the data stores in HA mode, for cluster configuration data resiliency.

Some Kubernetes cluster bootstrapping tools, such as **kubeadm**, by default, provision stacked etcd control plane nodes, where the data store runs alongside and shares resources with the other control plane components on the same control plane node.
> **Stacked etcd Topology**![[Stacked_etcd_Topology2023.png]]


For data store isolation from the control plane components, the bootstrapping process can be configured for an *external* etcd topology, where the data store is provisioned on a dedicated separate host, thus reducing the chances of an etcd failure.
> **External etcd Topology**![[External_etcd_Topology2023.png]]


Both stacked and external etcd topologies support HA configurations. etcd is based on the [Raft Consensus Algorithm](https://web.stanford.edu/~ouster/cgi-bin/papers/raft-atc14) which allows a collection of machines to work as a coherent group that can survive the failures of some of its members. At any given time, one of the nodes in the group will be the leader, and the rest of them will be the followers. etcd gracefully handles leader elections and can tolerate node failure, including leader node failures. Any node can be treated as a leader.
> **Leader and Followers**![[Leader_and_Followers2023.png]]

etcd is written in the Go programming language. In Kubernetes, besides storing the cluster state, etcd is also used to store <mark style="background: #BBFABBA6;">configuration details such as subnets, ConfigMaps, Secrets, etc.
</mark>

### **Worker Node Overview**
A **Worker Node** provides a running environment for client applications. These applications are microservices running as application containers.

In Kubernetes, application containers are encapsulated in Pods, controlled by the cluster Control Plane agents running on the control plane node. 

Pods are scheduled on worker nodes, where they find required compute, memory and storage resources to run, and networking to talk to each other and the outside world. 

A Pod is the smallest scheduling work unit in Kubernetes.

It is a logical collection of one or more containers scheduled together, and the collection can be started, stopped, or rescheduled as a single unit of work.

Also, in a multi-worker Kubernetes cluster, the network traffic between client users and the containerized applications deployed in Pods is handled directly by the worker nodes, and is not routed through the control plane node.

#### **Worker Node Components**
A worker node has the following components:
- Container Runtime
- Node Agent - kubelet
- Proxy - kube-proxy
- Add-ons for DNS, Dashboard user interface, cluster-level monitoring and logging.

##### **Worker Node Components: Container Runtime**
Although Kubernetes is described as a "container orchestration engine", it lacks the capability to directly handle and run containers. 
In order to manage a container's lifecycle, Kubernetes requires a **container runtime** on the node where a Pod and its containers are to be scheduled.
Runtimes are required on all nodes of a Kubernetes cluster, both control plane and worker. Kubernetes supports several container runtimes:
- [CRI-O ](https://cri-o.io/)
	  A lightweight container runtime for Kubernetes, supporting [quay.io](https://quay.io/) and [Docker Hub](https://hub.docker.com/) image registries.
- [containerd ](https://containerd.io/)
	  A simple, robust, and portable container runtime.
- [Docker Engine](https://www.docker.com/)
	  A popular and complex container platform which uses **containerd** as a container runtime.
- [Mirantis Container Runtime ](https://www.mirantis.com/software/container-runtime/)
	  Formerly known as the **Docker Enterprise Edition**.

##### **Worker Node Components: Node Agent - kubelet**
The *kubelet* is an agent running in both control plane nodes and worker nodes. It communicates with the Control Plane node. 

It receives Pod definitions, primarily from the API Server, and interacts with the container runtime on the node to run containers associated with the Pod.
It also monitors the health and resources of Pods running containers.

The *kubelet* connects to container runtimes through a plugin based interface - the [Container Runtime Interface](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md) (CRI).
The CRI consists of protocol buffers, gRPC API, libraries, and additional specifications and tools. 
In order to connect to interchangeable container runtimes, kubelet uses a **CRI shim**, an application which provides a clear abstraction layer between kubelet and the container runtime.

> **Container Runtime Interface (Retrieved from** [blog.kubernetes.io](http://blog.kubernetes.io/2016/12/container-runtime-interface-cri-in-kubernetes.html))![[Container_Runtime_Interface2023.png]]

As shown above, the kubelet acting as grpc client connects to the CRI shim acting as grpc server to perform container and image operations. The CRI implements two services: **ImageService** and **RuntimeService**. 
The **ImageService** is responsible for all the image-related operations, while the **RuntimeService** is responsible for all the Pod and container-related operations.

##### **Worker Node Components: kubelet - CRI shims**
Originally the kubelet agent supported only a couple of container runtimes, first the Docker Engine followed by rkt, through a unique interface model integrated directly in the kubelet source code.
However, this approach was not intended to last forever even though it was especially beneficial for Docker.
In time, Kubernetes started migrating towards a standardized approach to container runtime integration by introducing the CRI.
Kubernetes adopted a decoupled and flexible method to integrate with various container runtimes without the need to recompile its source code.
Any container runtime that implements the CRI could be used by Kubernetes to manage containers.

Shims are Container Runtime Interface (CRI) implementations, interfaces or adapters, specific to each container runtime supported by Kubernetes. Below we present some examples of CRI shims:

**cri-containerd**
cri-containerd allows containers to be directly created and managed with containerd at kubelet's request:
> **cri-containerd** (Retrieved from [blog.kubernetes.io](http://blog.kubernetes.io/2017/11/containerd-container-runtime-options-kubernetes.html))![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@cri-containerd2023.png]]

**CRI-O**
CRI-O enables the use of any Open Container Initiative (OCI) compatible runtime with Kubernetes, such as runC:
> **CRI-O** (Retrieved from [cri-o.io](http://cri-o.io/))
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@CRI-O2023.png]]

**dockershim** and **cri-dockerd**
Before Kubernetes release v1.24 the **dockershim** allowed containers to be created and managed by invoking the Docker Engine and its internal runtime containerd.
Due to Docker Engine's popularity, this shim has been the default interface used by kubelet. However, starting with Kubernetes release v1.24, the dockershim is no longer being maintained by the Kubernetes project, its specific code is removed from kubelet source code, thus will no longer be supported by the kubelet node agent of Kubernetes.
As a result, [Docker, Inc.,](https://www.docker.com/) and [Mirantis](https://www.mirantis.com/) have agreed to introduce and maintain a replacement adapter, **cri-dockerd** that would ensure that the Docker Engine will continue to be a container runtime option for Kubernetes, in addition to the Mirantis Container Runtime (MCR).
The introduction of cri-dockerd also ensures that both Docker Engine and MCR follow the same standardized integration method as the CRI-compatible runtimes.
>**dockershim** (Retrieved from [blog.kubernetes.io](http://blog.kubernetes.io/2017/11/containerd-container-runtime-options-kubernetes.html))![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@dockershim2023.png]]

Additional details about the deprecation process of the dockershim can be found on the [Updated: Dockershim Removal FAQ](https://kubernetes.io/blog/2022/02/17/dockershim-faq/) page.

##### **Worker Node Components: Proxy - kube-proxy**
The **kube-proxy** is the network agent which runs on each node, control plane and workers, responsible for dynamic updates and maintenance of all networking rules on the node. It abstracts the details of Pods networking and forwards connection requests to the containers in the Pods.

The kube-proxy is responsible for TCP, UDP, and SCTP stream forwarding or random forwarding across a set of Pod backends of an application, and it implements forwarding rules defined by users through Service API objects.

##### **Worker Node Components: Proxy - Add-ons**
**Add-ons** are cluster features and functionality not yet available in Kubernetes, therefore implemented through 3rd-party pods and services.

- **DNS  
    **Cluster DNS is a DNS server required to assign DNS records to Kubernetes objects and resources.
- **Dashboard**   
    A general purpose web-based user interface for cluster management.
- **Monitoring**   
    Collects cluster-level container metrics and saves them to a central data store.
- **Logging**   
    Collects cluster-level container logs and saves them to a central log store for analysis.

#### **Networking Challenges**
Decoupled microservices based applications rely heavily on networking in order to mimic the tight-coupling once available in the monolithic era. Networking, in general, is not the easiest to understand and implement. Kubernetes is no exception - as a containerized microservices orchestrator it needs to address a few distinct networking challenges:
- Container-to-Container communication inside Pods
- Pod-to-Pod communication on the same node and across cluster nodes
- Service-to-Pod communication within the same namespace and across cluster namespaces
- External-to-Service communication for clients to access applications in a cluster

All these networking challenges must be addressed before deploying a Kubernetes cluster.

##### **Container-to-Container Communication Inside Pods**
Making use of the underlying host operating system's kernel virtualization features, a container runtime creates an isolated network space for each container it starts.
On Linux, this isolated network space is referred to as a **network namespace**.
A network namespace can be shared across containers, or with the host operating system.

When a grouping of containers defined by a Pod is started, a special infrastructure **Pause container** is initialized by the Container Runtime for the sole purpose of creating a network namespace for the Pod. 
All additional containers, created through user requests, running inside the Pod will share the Pause container's network namespace so that they can all talk to each other via localhost.

##### **Pod-to-Pod Communication Across Nodes**
In a Kubernetes cluster Pods, groups of containers, are scheduled on nodes in a nearly unpredictable fashion.
Regardless of their host node, Pods are expected to be able to communicate with all other Pods in the cluster, all this without the implementation of Network Address Translation (NAT).
This is a fundamental requirement of any networking implementation in Kubernetes.

The Kubernetes network model aims to reduce complexity, and it treats Pods as VMs on a network, where each VM is equipped with a network interface - thus each Pod receiving a unique IP address.
This model is called "**IP-per-Pod**" and ensures Pod-to-Pod communication, just as VMs are able to communicate with each other on the same network.

Let's not forget about containers though. They share the Pod's network namespace and must coordinate ports assignment inside the Pod just as applications would on a VM, all while being able to communicate with each other on **localhost** - inside the Pod.
However, containers are integrated with the overall Kubernetes networking model through the use of the [Container Network Interface](https://github.com/containernetworking/cni) (CNI) supported by [CNI plugins](https://github.com/containernetworking/cni#3rd-party-plugins).

CNI is a set of specifications and libraries which allow plugins to configure the networking for containers.
While there are a few [core plugins](https://github.com/containernetworking/plugins#plugins), most CNI plugins are 3rd-party Software Defined Networking (SDN) solutions implementing the Kubernetes networking model. 
In addition to addressing the fundamental requirement of the networking model, some networking solutions offer support for Network Policies.
[Flannel](https://github.com/coreos/flannel/), [Weave](https://www.weave.works/oss/net/), [Calico](https://www.tigera.io/project-calico/) are only a few of the SDN solutions available for Kubernetes clusters.

>**Container Network Interface (CNI)** **Core Plugins**![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@Container_Network_Interface__CNI__Core_Plugins2023.png]]

The container runtime offloads the IP assignment to CNI, which connects to the underlying configured plugin, such as Bridge or MACvlan, to get the IP address.
Once the IP address is given by the respective plugin, CNI forwards it back to the requested container runtime.

For more details, you can explore the [Kubernetes documentation](https://kubernetes.io/docs/concepts/cluster-administration/networking/).

##### **External-to-Pod Communication**
A successfully deployed containerized application running in Pods inside a Kubernetes cluster may require accessibility from the outside world. 
Kubernetes enables external accessibility through **Services**, complex encapsulations of network routing rule definitions stored in **iptables** on cluster nodes and implemented by **kube-proxy** agents.
By exposing services to the external world with the aid of **kube-proxy**, applications become accessible from outside the cluster over a virtual IP address and a dedicated port number.


##### Learning Objectives (Review)
You should now be able to:
- Discuss the Kubernetes architecture.
- Explain the different components of the control plane and worker nodes.
- Discuss cluster state management with etcd.
- Review the Kubernetes network setup requirements.

---
# Installing Kubernetes
 
## Chapter Overview
In this chapter, we will explore Kubernetes cluster deployment considerations. 
First, we will learn about Kubernetes cluster configuration options, followed by infrastructure requirements and installation tools specific to various cluster deployment models.

###### Learning Objectives
By the end of this chapter, you should be able to:
- Discuss Kubernetes configuration options.
- Discuss infrastructure considerations before installing Kubernetes.
- Discuss infrastructure choices for a Kubernetes cluster deployment.
- Review Kubernetes installation tools and certified solutions.

### Kubernetes Configuration
Kubernetes can be installed using different cluster configurations. The major installation types are described below:
- **All-in-One Single-Node Installation**  
    In this setup, all the control plane and worker components are installed and running on a single-node. While it is useful for learning, development, and testing, it is not recommended for production purposes.
- **Single-Control Plane and Multi-Worker Installation**  
    In this setup, we have a single-control plane node running a stacked etcd instance. Multiple worker nodes can be managed by the control plane node.
- **Single-Control Plane with Single-Node etcd, and Multi-Worker Installation**  
    In this setup, we have a single-control plane node with an external etcd instance. Multiple worker nodes can be managed by the control plane node.
- **Multi-Control Plane and Multi-Worker Installation**  
    In this setup, we have multiple control plane nodes configured for High-Availability (HA), with each control plane node running a stacked etcd instance. The etcd instances are also configured in an HA etcd cluster and multiple worker nodes can be managed by the HA control plane.
- **Multi-Control Plane with Multi-Node etcd, and Multi-Worker Installation**  
    In this setup, we have multiple control plane nodes configured in HA mode, with each control plane node paired with an external etcd instance. The external etcd instances are also configured in an HA etcd cluster, and multiple worker nodes can be managed by the HA control plane. This is the most advanced cluster configuration recommended for production environments. 

As the Kubernetes cluster's complexity grows, so does its hardware and resources requirements. While we can deploy Kubernetes on a single host for learning, development, and possibly testing purposes, the community recommends multi-host environments that support High-Availability control plane setups and multiple worker nodes for client workload for production purposes.

### Infrastructure for Kubernetes Installation
nce we decide on the installation type, we need to decide on the infrastructure. 
Infrastructure related decisions are typically guided by the desired environment type, either learning or production environment.
For infrastructure, we need to decide on the following:
- Should we set up Kubernetes on bare metal, public cloud, private, or hybrid cloud?
- Which underlying OS should we use? Should we choose a Linux distribution - Red Hat-based or Debian-based, or Windows?
- Which networking solution (CNI) should we use?

Explore the [Kubernetes documentation](https://kubernetes.io/docs/setup/) for details on choosing the right solution.

### Installing *Local* Learning Clusters
There are a variety of installation tools allowing us to deploy single- or multi-node Kubernetes clusters on our workstations, for learning and development purposes.
While not an exhaustive list, below we enumerate a few popular ones:
- [Minikube](https://minikube.sigs.k8s.io/docs/)   
    Single- and multi-node local Kubernetes cluster, recommended for a learning environment deployed on a single host.
- [Kind](https://kind.sigs.k8s.io)   
    Multi-node Kubernetes cluster deployed in Docker containers acting as Kubernetes nodes, recommended for a learning environment.
- [Docker Desktop](https://www.docker.com/products/docker-desktop)   
    Including a local Kubernetes cluster for Docker users. 
- [MicroK8s](https://microk8s.io/)   
    Local and cloud Kubernetes cluster for developers and production, from Canonical.
- [K3S](https://k3s.io/)   
    Lightweight Kubernetes cluster for local, cloud, edge, IoT deployments, originally from Rancher, currently a CNCF project.

Minikube is an easy and flexible method to create a local Kubernetes setup. We will be using it extensively in this course to manage certain aspects of a Kubernetes cluster, while taking advantage of several automated features designed to simplify the user interaction with the Kubernetes environment and the containerized applications deployed to the cluster.

### Installing *Production* Clusters with Deployment Tools
When it comes to production ready solutions, there are several recommended tools for Kubernetes clusters bootstrapping and a few that are also capable of provisioning the necessary hosts on the underlying infrastructure.

Let's take a look at the most popular installation tools available:

**kubeadm**
[kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) is a first-class citizen of the Kubernetes ecosystem.
It is a secure and recommended method to bootstrap a multi-node production ready Highly Available Kubernetes cluster, on-premises or in the cloud.
kubeadm can also bootstrap a single-node cluster for learning.
It has a set of building blocks to set up the cluster, but it is easily extendable to add more features.
Please note that kubeadm does not support the provisioning of hosts - they should be provisioned separately with a tool of our choice.
![[logo-kubeadm.png]]


**kubespray**
[kubespray](https://kubernetes.io/docs/setup/production-environment/tools/kubespray/) (formerly known as kargo) allows us to install Highly Available production ready Kubernetes clusters on AWS, GCP, Azure, OpenStack, vSphere, or bare metal.
kubespray is based on Ansible, and is available on most Linux distributions. 
It is a [Kubernetes Incubator](https://github.com/kubernetes-sigs/kubespray/) project.
![[kubespray-logo-text-clear.png]]

**kops**
[kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/) enables us to create, upgrade, and maintain production-grade, Highly Available Kubernetes clusters from the command line.
It can provision the required infrastructure as well.
Currently, AWS is officially supported. 
Support for DigitalOcean and OpenStack is in beta, Azure and GCE is in alpha support, and other platforms are planned for the future. Explore the [kops project](https://github.com/kubernetes/kops/) for more details.
![[logo-kops.jpg]]

In addition, for a manual installation approach, the _[Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)_ GitHub project by [Kelsey Hightower](https://twitter.com/kelseyhightower) is an extremely helpful installation guide and resource.
The project aims to teach all the detailed steps involved in the bootstrapping of a Kubernetes cluster, steps that are otherwise automated by various tools mentioned in this chapter and obscured from the end user.

### Production Clusters from Certified Solutions Providers
The growing popularity of Kubernetes accelerated its adoption by many cloud services providers together with hosted platforms of certified Kubernetes distributions.
There are well over 200 managed [certified Kubernetes](https://kubernetes.io/partners/) services providers today, as many more organizations became Kubernetes partners, joining the list of initial providers of hosted Kubernetes solutions:

**Hosted Solutions**  
Hosted Solutions providers fully manage the provided software stack, while the user pays hosting and management charges.
Popular vendors providing hosted solutions for Kubernetes are (listed in alphabetical order):
- [Alibaba Cloud Container Service for Kubernetes](https://www.alibabacloud.com/product/kubernetes) (ACK)
- [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS)
- [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/) (AKS)
- [DigitalOcean Kubernetes](https://www.digitalocean.com/products/kubernetes/)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) (GKE)
- [IBM Cloud Kubernetes Service](https://www.ibm.com/cloud/kubernetes-service/)
- [Oracle Container Engine for Kubernetes](https://www.oracle.com/cloud-native/container-engine-kubernetes/) (OKE)
- [Platform9 Managed Kubernetes](https://platform9.com/managed-kubernetes/) (PMK)
- [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)
- [VMware Tanzu Kubernetes Grid](https://tanzu.vmware.com/kubernetes-grid)

**Partners**
Additional [Partners](https://kubernetes.io/partners/) providing managed Kubernetes services and platforms (listed in alphabetical order):
- Altoros
- Aqua Security
- Canonical
- D2IQ
- Dell Technologies Consulting
- Deloitte
- Fujitsu
- GitLab
- HPE
- Inovex
- Kubermatic
- Kublr
- Mirantis
- Nirmata
- Rancher
- SAP
- Sysdig
- Weaveworks

**Turnkey Cloud Solutions**
[Turnkey Cloud Solutions](https://kubernetes.io/docs/setup/production-environment/turnkey-solutions/) install production ready Kubernetes clusters on cloud infrastructure:
- Linode Kubernetes Engine
- Nirmata Managed Kubernetes
- Nutanix Karbon
- Vultr Kubernetes Engine

---
# Chapter 6. Minikube - Installing Local Kubernetes Clusters
## Introduction
**Chapter Overview**
[Minikube](https://minikube.sigs.k8s.io/) is one of the easiest, most flexible and popular methods to run an all-in-one or a multi-node local Kubernetes cluster, isolated by Virtual Machines (VM) or Containers, run directly on our workstations.
Minikube is the tool responsible for the installation of Kubernetes components, cluster bootstrapping, and cluster tear-down when no longer needed.
It includes additional features aimed to ease the user interaction with the Kubernetes cluster, but nonetheless, it initializes for us a fully functional, non-production, Kubernetes cluster extremely convenient for learning purposes. Minikube can be installed on native macOS, Windows, and many Linux distributions.

In this chapter, we will explore the requirements to install Minikube locally on our workstation.

![[Minikube_logo.png]]

###### Learning Objectives
By the end of this chapter, you should be able to:
- Understand Minikube.
- Install Minikube on the native OS of your workstation.
- Verify the local installation.

## What Is Minikube?
Minikube is one of the easiest, most flexible and popular methods to run an all-in-one or a multi-node local Kubernetes cluster directly on our local workstations. It installs and runs on any native OS such as Linux, macOS, or Windows.

However, in order to fully take advantage of all the features Minikube has to offer, a [Type-2 Hypervisor](https://en.wikipedia.org/wiki/Hypervisor) or a Container Runtime should be installed on the local workstation, to run in conjunction with Minikube.

The role of the hypervisor or container runtime is to offer an isolated infrastructure for the Minikube Kubernetes cluster components, that is easily reproducible, easy to use and tear down.

This isolation of the cluster components from our daily environment ensures that once no longer needed, the Minikube components can be safely removed leaving behind no configuration changes to our workstation, thus no traces of their existence.

This does not mean, however, that we are responsible for the provisioning of any VMs or containers with guest operating systems with the help of the hypervisor or container runtime.

Minikube includes the necessary adapters to interact directly with the isolation software of choice to build all its infrastructure as long as the Type-2 Hypervisor or Container Runtime is installed on our workstation.

Minikube is built on the capabilities of the [libmachine](https://github.com/docker/machine/tree/master/libmachine) library originally designed by Docker to build [Virtual Machine container hosts](https://github.com/docker/machine) on any physical infrastructure.
In time Minikube became very flexible, supporting several hypervisors and container runtimes, depending on the host workstation's native OS.

For those who feel more adventurous, Minikube can be installed without an isolation software, on bare-metal, which may result in permanent configuration changes to the host OS.
To prevent such permanent configuration changes, a second form of isolation can be achieved by installing Minikube inside a Virtual Machine provisioned with a Type-2 Hypervisor of choice, and a desktop guest OS of choice (with enabled GUI).
As a result, when installed inside a VM, Minikube will end up making configuration changes to the guest environment, still isolated from the host workstation.
Therefore, now we have two distinct methods to isolate the Minikube environment from our host workstation.

The isolation software can be specified by the user with the **--driver** option, otherwise Minikube will try to find a preferred method for the host OS of the workstation.

Once decided on the isolation method, the next step is to determine the required number of Kubernetes cluster nodes, and their sizes in terms of CPU, memory, and disk space.
Minikube invokes the hypervisor of choice to provision the infrastructure VM(s) which will host the Kubernetes cluster node(s), or the runtime of choice to run infrastructure container(s) that host the cluster node(s).
Keep in mind that Minikube now supports all-in-one single-node and multi-node clusters. Regardless of the isolation method and the expected cluster and node sizes, a local Minikube Kubernetes cluster will ultimately be impacted and/or limited by the physical resources of the host workstation.
We have to be mindful of the needs of the host OS and any utilities it may be running, then the needs of the hypervisor or the container runtime, and finally the remaining resources that can be allocated to our Kubernetes cluster.
For a learning environment the recommendations are that a Kubernetes node has 2 CPU cores (or virtual CPUs) at a minimum, at least 2 GB of RAM memory (with 4 - 8 GB of RAM recommended for optimal usage), and 20+ GB of disk storage space.
When migrating towards a larger, more dynamic, production grade cluster, these resource values should be adjusted accordingly.
The Kubernetes nodes are expected to access the internet as well, for software updates, container image downloads, and for client accessibility.

Following the node(s)' provisioning phase, Minikube invokes [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/), to bootstrap the Kubernetes cluster components inside the previously provisioned node(s).
We need to ensure that we have the necessary hardware and software required by Minikube to build our environment.

### Requirements for Running Minikube
Below we outline the requirements to run Minikube on our local workstation:
- VT-x/AMD-v virtualization must be enabled on the local workstation, and/or verify if it is supported.
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)  
    **kubectl** is a binary used to access and manage any Kubernetes cluster. It is installed through Minikube and accessed through the **minikube kubectl** command, or it can be installed separately and run as a standalone tool. We will explore **kubectl** installation and usage in future chapters.
- Type-2 Hypervisor or Container Runtime  
    Without a specified driver, Minikube will try to find an installed hypervisor or a runtime, in the following order of preference (on a Linux host): docker, kvm2, podman, vmware, and virtualbox.
     If multiple isolation software installations are found, such as docker and virtualbox, Minikube will pick docker over virtualbox if no desired driver is specified by the user. Hypervisors and Container Runtimes supported by various native workstation OSes:  
    - On Linux [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [KVM2](https://www.linux-kvm.org/page/Main_Page), and [QEMU](https://www.qemu.org/) hypervisors, or [Docker](https://docs.docker.com/engine/install/) and [Podman](https://podman.io/getting-started/installation.html) runtimes  
    - On macOS [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [HyperKit](https://github.com/moby/hyperkit), [VMware Fusion](http://www.vmware.com/products/fusion.html), [Parallels](https://www.parallels.com/), and [QEMU](https://www.qemu.org/) hypervisors, or [Docker](https://docs.docker.com/desktop/mac/install/) runtime  
    - On Windows [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v), [VMware Workstation](https://www.vmware.com/in/products/workstation-pro/workstation-pro-evaluation.html), and [QEMU](https://www.qemu.org/) hypervisors, or [Docker](https://docs.docker.com/desktop/windows/install/) runtime.

_**NOTE:** Minikube supports a **[--driver=none](https://minikube.sigs.k8s.io/docs/drivers/none/)** (on Linux) option that runs the Kubernetes components bare-metal, directly on the host OS and not inside a VM. With this option a Docker installation is required and a Linux OS on the local workstation, but no hypervisor installation. This driver is recommended for advanced users._

Read more about Minikube from the official [Minikube documentation](https://minikube.sigs.k8s.io/docs/), the official [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#minikube), or [GitHub](https://github.com/kubernetes/minikube).

## Installing Minikube on Linux
The course recommends working with a VirtualBox hypervisor for the sake of convenience.

I will be attempting to set it up and running with the Docker Engine as i already have it installed on my Linux machine running Debian 12.4 Bookworm.

Following the documentation below to install *minikube*:
https://minikube.sigs.k8s.io/docs/start/

```shell
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

sudo dpkg -i minikube_latest_amd64.deb
```


https://stackoverflow.com/questions/47854463/docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socke

After following the steps in the above link, adding the $USER to the docker group, i am able to finally run `minikube start --driver=docker` without having to use docker as root.
![[Pasted image 20240206122751.png]]

End result:
![[Pasted image 20240206123051.png]]

Running `minikube status` returns the desired output:
![[Pasted image 20240206123217.png]]

Running `minikube stop` will stop Minikube:
![[Pasted image 20240206123315.png]]

### Demo: Getting Started with Minikube on Linux

![[8358fa40-08c5-40a4-b701-92affa8e7447-mp4_720p.mp4]]

### Advanced Minikube Features

The **minikube start** by default selects a driver isolation software, such as a hypervisor or a container runtime, if one (VitualBox) or multiple are installed on the host workstation. In addition it downloads the latest Kubernetes version components.

With the selected driver software it provisions a single VM named **minikube** (with hardware profile of CPUs=2, Memory=6GB, Disk=20GB) or container to host the default single-node all-in-one Kubernetes cluster.

Once the node is provisioned, it bootstraps the Kubernetes control plane (with the default kubeadm tool), and it installs the latest version of the default container runtime, Docker, that will serve as a running environment for the containerized applications we will deploy to the Kubernetes cluster.

The **minikube start** command generates a <mark style="background: #FFF3A3A6;">default</mark> **minikube** cluster with the specifications described above and it will store these specs so that we can restart the default cluster whenever desired. 
The object that stores the specifications of our cluster is called a **profile**.

With the introduction of **profiles**, Minikube allows users to create custom reusable clusters that can all be managed from a single command line client.

The **minikube profile** command allows us to view the status of all our clusters in a table formatted output. Assuming we have created only the default **minikube** cluster, we could list the properties that define the default profile with:

```bash
minikube profile list
```

Which returns the following output in the CLI:
![[Pasted image 20240206143026.png]]

This table presents the columns associated with the default properties such as:
The *profile name*: minikube,
The *isolation driver*: docker,
The *container runtime*: Docker,
The *Kubernetes version*: v1.25.3, 
The *status of the cluster* - running or stopped.
The table also displays the *number of nodes*: 1 by default,
the *private IP address* of the minikube cluster's control plane,
and the *secure port* that exposes the API Server to cluster control plane components, agents and clients: 8443.

What if we desire to create several reusable clusters instead, with other drivers (Docker or Podman for node isolation, or different Kubernetes versions (v1.23.3 or v1.24.4), another runtime (cri-o or containerd), and possibly 2, 3, or more nodes (if permitted by the resources of our host system)? 
What if we desire to further customize the cluster with a specific networking option or plugin?

The **minikube start**  command allows us to create such custom profiles with the **--profile** or **-p** flags.

Several of the isolation drivers support creation of node VMs or node containers of custom sizes as well, features that we will not explore in this course as not all are very stable at the time of this writing.

Below are a few examples of more complex **start** commands that allow custom clusters to be created with Minikube.
They assume that the desired driver software (Docker and/or Podman) has been installed on the host workstation.
There is no need to download the desired CNI (network plugin) or the container runtime, they will be set up and enabled by Minikube on our behalf:
```bash
minikube start --kubernetes-version=v1.23.3 \  
--driver=podman --profile minipod
```

```bash
minikube start --nodes=2 --kubernetes-version=v1.24.4 \
--driver=docker --profile doubledocker
```

```bash
minikube start --driver=virtualbox --nodes=3 --disk-size=10g \  
--cpus=2 --memory=4g --kubernetes-version=v1.25.1 --cni=calico \  
--container-runtime=cri-o -p multivbox
```

```bash
minikube start --driver=docker --cpus=6 --memory=8g \  
--kubernetes-version="1.24.4" -p largedock
```

```bash
minikube start --driver=virtualbox -n 3 --container-runtime=containerd \ 
--cni=calico -p minibox
```

Once multiple cluster profiles are available (the default **minikube** and custom **minibox**), the profiles table will look like this:

![[Pasted image 20240206145229.png]]

The **active** marker indicates the target cluster profile of the minikube command line tool. The target cluster can be set to **minibox** with the following command:
```bash
minikube profile minibox
```

The target cluster can be set to the default **minikube** with one of the following commands:
```bash
minikube profile minikube
```

```bash
minikube profile default
```


Most **minikube** commands, such as start, stop, node, etc. are profile aware, meaning that the user is required to specify the target cluster of the command, through its profile name.
The default **minikube** cluster, however, can be managed without specifying its profile name.
Stopping and re-starting the two clusters listed above, the **minibox** cluster and the default **minikube**:

```bash
minikube stop -p minibox
```

```bash
minikube start -p minibox
```

```bash
minikube stop
```

```bash
minikube start
```


>Additional helpful **minikube** commands:

To display the version of the current Minikube installation:
```bash
minikube version
```
![[Pasted image 20240206145634.png]]


Completion is a helpful post installation configuration to enable the **minikube** command to respond to typical auto-completion mechanisms, such as completing a command in the terminal by pressing the TAB key.
To enable completion for the bash shell on Ubuntu: #Minikube_auto_completion
```bash
sudo apt install bash-completion
```

```bash
source /etc/bash_completion
```

```bash
source <(minikube completion bash)
```

If needed, also run the following command:
```bash
minikube completion bash
```


A command that allows users to *list the nodes of a cluster*, *add new control plane* or *worker nodes*, *delete* existing cluster nodes, *start or stop individual nodes of a cluster*: #Minikube_list_nodes
```bash
minikube node list
```
![[Pasted image 20240206145956.png]]

```bash
minikube node list -p minibox
```
![[Pasted image 20240206150032.png]]

To display the cluster control plane node's IP address, or another node's IP with the **--node** or **-n** flags: #Minikube_display_control_plane_IP
![[Pasted image 20240206150106.png]]

![[Pasted image 20240206150121.png]]

![[Pasted image 20240206150127.png]]

When a cluster configuration is no longer of use, the cluster's profile can be deleted.
It is also a profile aware command - it deletes the default **minikube** cluster if no profile is specified, or a custom cluster if its profile is specified: #Minikube_delete_cluster_profile
![[Pasted image 20240206150400.png]]

![[Pasted image 20240206150407.png]]

For additional commands and usage options please visit the [Minikube command line reference](https://minikube.sigs.k8s.io/docs/commands/). #Minikube_command_line_reference

##### Demo: Exploring Minikube Profiles
![[9c2e84a1-4434-4220-bb44-82e680681110-mp4_720p.mp4]]
What if we wanted to provision a different cluster, with a different size, runtime and driver?
For that, we need to run `minikube start` with a few configuration options:
```bash
minikube start --nodes=2 --driver=docker --kubernetes-version=1.24.4 --container-runtime=cri-o --profile minidock
```
The above command is going to provision a cluster that has 2 nodes, with the docker driver and a Kubernetes version of 1.24.4, container runtime cri-o and with the default compute resources CPUs=2, Memory=2200MB.
![[Pasted image 20240206154823.png]]
Once the provisioning is done, we can run the `minikube profile list` command in order to see the new cluster is reflected in the profiles list:
![[Pasted image 20240206154942.png]]
As we can see, the `minidock` cluster has indeed been provisioned and is currently running.

Currently, we can see that the Active selection is currently set to the `minikube` cluster, which means the CLI commands will be ran on the selected `minikube` cluster.

Running `sudo docker ps` will list all of the Docker containers currently running:
![[Pasted image 20240206155252.png]]
As we can see, two Docker processes are currently running, which are the two nodes that we have previously provisioned via the Minikube command. 

The `minidock` container will be our ***Control Plane Node*** whereas the `minidock-m02` will be our ***Worker Node***.

Since we are using the Docker driver instead of a Virtual Machine, the nodes reside inside Docker Containers instead of virtual machines.

In order to remove the `minidock` profile, we run the following command:
```bash
minikube delete -p minidock
```
![[Pasted image 20240206155717.png]]

---
# Chapter 7. Accessing Minikube

In this chapter, we will learn about different methods of accessing a Kubernetes cluster.

We can use a variety of external clients or custom scripts to access our cluster for administration purposes. We will explore **kubectl** as a CLI tool to access the Minikube Kubernetes cluster, the **Kubernetes Dashboard** as a web-based user interface to interact with the cluster, and the **curl** command with proper credentials to access the cluster via APIs.


###### Learning Objectives
By the end of this chapter, you should be able to:
- Compare methods to access a Kubernetes cluster.
- Access the Minikube Kubernetes cluster with kubectl.
- Access the Minikube Kubernetes cluster from the Dashboard.
- Access the Minikube Kubernetes cluster via APIs.


## Accessing Minikube
Any healthy running Kubernetes cluster can be accessed via any one of the following methods:
- Command Line Interface (CLI) tools and scripts
- Web-based User Interface (Web UI) from a web browser
- APIs from CLI or programmatically

These methods are applicable to all Kubernetes clusters.

#### Accessing Minikube: Command Line Interface (CLI)
**[kubectl](https://kubernetes.io/docs/reference/kubectl/overview/)** is the Kubernetes Command Line Interface (CLI) client to manage cluster resources and applications. It is very flexible and easy to integrate with other systems, therefore it can be used standalone, or part of scripts and automation tools. Once all required credentials and cluster access points have been configured for **kubectl**, it can be used remotely from anywhere to access a cluster.

We will be using **kubectl** extensively to deploy applications, manage and configure Kubernetes resources.

#### Accessing Minikube: Web-based User Interface (Web UI)
The **[Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)** provides a Web-based User Interface (Web UI) to interact with a Kubernetes cluster to manage resources and containerized applications.
While not as flexible as the **kubectl** CLI client tool, it is still a preferred tool to users who are not as proficient with the CLI.
![[ui-dashboard.png]]
#### Accessing Minikube: APIs
The main component of the Kubernetes control plane is the **API Server**, responsible for exposing the Kubernetes APIs.
The APIs allow operators and users to directly interact with the cluster.
Using both CLI tools and the Dashboard UI, we can access the API server running on the control plane node to perform various operations to modify the cluster's state. 
The API Server is accessible through its endpoints by agents and users possessing the required credentials.

Below, we can see the representation of the HTTP API directory tree of Kubernetes:
**HTTP API Directory Tree of Kubernetes**
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@LFS158_2023_CourseImage_Chapter-7-02.png]]

HTTP API directory tree of Kubernetes can be divided into three independent group types:
- Core group **(/api/v1)**
	   This group includes objects such as Pods, Services, Nodes, Namespaces, ConfigMaps, Secrets, etc.

- Named group
	  This group includes objects in **/apis/\$NAME/$VERSION** format. These different API versions imply different levels of stability and support:  
    - _Alpha level_ - it may be dropped at any point in time, without notice. For example, **/apis/batch/v2alpha1**.  
    - _Beta level_ - it is well-tested, but the semantics of objects may change in incompatible ways in a subsequent beta or stable release. For example, **/apis/certificates.k8s.io/v1beta1**.  
    - _Stable level_ - appears in released software for many subsequent versions. For example, **/apis/networking.k8s.io/v1**.

- System-wide
	  This group consists of system-wide API endpoints, like **/healthz**, **/logs**, **/metrics**, **/ui**, etc.

We can access an API Server either directly by calling the respective API endpoints, using the CLI tools, or the Dashboard UI.

#### kubectl
**kubectl** allows us to manage local Kubernetes clusters like the Minikube cluster, or remote clusters deployed in the cloud.
It is generally installed before installing and starting Minikube, but it can also be installed after the cluster bootstrapping step.

A Minikube installation has its own kubectl CLI installed and ready to use.
However, it is somewhat inconvenient to use as the **kubectl** command becomes a subcommand of the **minikube** command.
Users would be required to type longer commands, such as `minikube kubectl --<subcommand> <object-type> <object-name> -o --option`, instead of just `kubectl <subcommand> <object-type> <object-name> -o --option`.
While a simple solution would be to set up an alias, the recommendation is to run the kubectl CLI tool as a standalone installation.

https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

Once separately installed, **kubectl** receives its configuration automatically for Minikube Kubernetes cluster access.
However, in different Kubernetes cluster setups, we may need to manually configure the cluster access points and certificates required by **kubectl** to securely access the cluster.

Additional details about the **kubectl** command line client can be found in the [kubectl book](https://kubectl.docs.kubernetes.io/), the [Kubernetes official documentation](https://kubernetes.io/docs/reference/kubectl/), or its [GitHub repository](https://github.com/kubernetes/kubectl).

- Kubectl is the Kubernetes cli
- Kubectl provides a swiss army knife of functionality for working with Kubernetes clusters
- Kubectl may be used to deploy and manage applications on Kubernetes
- Kubectl may be used for scripting and building higher-level frameworks

#### kubectl Configuration File
To access the Kubernetes cluster, the **kubectl** client needs the control plane node endpoint and appropriate credentials to be able to securely interact with the API Server running on the control plane node.
While starting Minikube, the startup process creates, by default, a configuration file, **config**, inside the **.kube** directory (often referred to as the **[kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)**), which resides in the user's **home** directory.
The configuration file has all the connection details required by **kubectl**.
By default, the **kubectl** binary parses this file to find the control plane node's connection endpoint, along with the required credentials. Multiple **kubeconfig** files can be configured with a single **kubectl** client. To look at the connection details, we can either display the content of the **~/.kube/config** file (on Linux) or run the following command (the output is redacted for readability):
`kubectl config view`
![[Pasted image 20240206185918.png]]
The kubeconfig includes the API Server's endpoint **server:** https://192.168.99.100:8443 and the **minikube** user's client authentication **key** and **certificate** data.

Once **kubectl** is installed, we can display information about the Minikube Kubernetes cluster with the **kubectl cluster-info** command:
`kubectl cluster-info`
![[Pasted image 20240206190233.png]]
You can find more details about the **kubectl** command line options [here](https://kubernetes.io/docs/reference/kubectl/overview/).

Although for the Kubernetes cluster installed by Minikube the **~/.kube/config** file gets created automatically, this is not the case for Kubernetes clusters installed by other tools.
In other cases, the config file has to be created manually and sometimes re-configured to suit various networking and client/server setups.


#### Kubernetes Dashboard
The **[Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)** provides a web-based user interface for Kubernetes cluster management.
Minikube installs the Dashboard as an addon, but it is disabled by default. 
Prior to using the Dashboard we are required to enable the Dashboard addon, together with the metrics-server addon, a helper addon designed to collect usage metrics from the Kubernetes cluster. 
To access the dashboard from Minikube, we can use the **minikube dashboard** command, which opens a new tab in our web browser displaying the Kubernetes Dashboard, but only after we list, enable required addons, and verify their state:

`minikube addons list`

`minikube addons enable metrics-server`

`minikube addons enable dashboard`

`minikube addons list`

`minikube dashboard`

![[ui-dashboard 1.png]]
![[Pasted image 20240206190946.png]]

#### APIs with 'kubectl proxy'
Issuing the **kubectl proxy** command, **kubectl** authenticates with the API server on the control plane node and makes services available on the default proxy port **8001**.
![[Pasted image 20240207140117.png]]

It locks the terminal for as long as the proxy is running, unless we run it in the background (with `kubectl proxy &`).

When **kubectl proxy** is running, we can send requests to the API over the **localhost** on the default proxy port **8001** (from another terminal, since the proxy locks the first terminal when running in foreground):
![[Pasted image 20240207140245.png]]

`curl http://localhost:8001/`
![[Pasted image 20240207140324.png]]

With the above **curl** request, we requested all the API endpoints from the API server. Clicking on the link above (in the **curl** command), it will open the same listing output in a browser tab.

![[Pasted image 20240207181155.png]]

![[Pasted image 20240207181258.png]]

![[Pasted image 20240207181330.png]]

![[Pasted image 20240207181349.png]]

![[Pasted image 20240207181408.png]]

#### APIs with Authentication
When not using the **kubectl proxy**, we need to authenticate to the API Server when sending API requests. We can authenticate by providing a **Bearer Token** when issuing a **curl** command, or by providing a set of **keys** and **certificates**.

A *Bearer Token* is an access token that can be generated by the authentication server (the API Server on the control plane node) at the client's request. Using that token, the client can securely communicate with the Kubernetes API Server without providing additional authentication details, and then, access resources. The token may need to be provided again for subsequent resource access requests.

We are going to be creating an access token for the *default* ServiceAccount, and granting special permission to access the root directory of the API (special permission that was not necessary when the `kubectl proxy` was used earlier).
The special permission will be set through a *Role Based Access Control* (RBAC) policy.
The policy is the `clusterrole` defined below, which is granted through the `clusterrolebinding` definition.
The special permission is only needed to access the root directory of the API, but not needed to access */api*, */apis*, or other subdirectories:

```shell
export TOKEN=$(kubectl create token default)
```

```shell
kubectl create clusterrole api-access-root --verb=get --non-resource-url=/*
```
![[Pasted image 20240207184655.png]]

```shell
kubectl create clusterrolebinding api-access-root --clusterrole api-access-root --serviceaccount=default:default
```
![[Pasted image 20240207184716.png]]

Retrieving the API Server endpoint:
```shell
export APISERVER=$(kubectl config view | grep https | cut -f 2- -d ":" | tr -d " ")
```

Confirming that the `APISERVER` stored the same IP as the Kubernetes control plane IP:
![[Pasted image 20240207185025.png]]
We can see that they do have the same IP.

Then, we can access the API Server using the `curl` command:
```shell
curl $APISERVER --header "Authorization: Bearer $TOKEN" --insecure
```
Which should return the API endpoints for us:
![[Pasted image 20240207185216.png]]

We can run additional **curl** commands to retrieve details about specific API groups as follows. These commands should work even without the special permission defined above and granted to the default ServiceAccount associated with the access token:

```shell
curl $APISERVER/api/v1 --header "Authorization: Bearer $TOKEN" --insecure
```

```shell
curl $APISERVER/apis/apps/v1 --header "Authorization: Bearer $TOKEN" --insecure
```

```shell
curl $APISERVER/healthz --header "Authorization: Bearer $TOKEN" --insecure
```

```shell
curl $APISERVER/metrics --header "Authorization: Bearer $TOKEN" --insecure
```

Instead of the **access token,** we can extract the client certificate, client key, and certificate authority data from the **.kube/config** file. Once extracted, they can be encoded and then passed with a **curl** command for authentication. The new **curl** command would look similar to the example below. Keep in mind, however, that the example command below would only work with the base 64 encoded client certificate, key and certificate authority data, and it is provided only for illustrative purposes.

```shell
curl $APISERVER --cert encoded-cert --key encoded-key --cacert encoded-ca
```


### DEMO: Accessing the Kubernetes API with kubectl
https://kubernetes.io/docs/reference/access-authn-authz/

![[f781f2ec-8e70-4123-a2b8-c3dd7adfc219-mp4_720p.mp4]]

---
# Chapter 8. Kubernetes Building Blocks
### Chapter Overview
In this chapter, we will explore the Kubernetes object model and describe some of its fundamental building blocks, such as Nodes, Namespaces, Pods, ReplicaSets, Deployments, DaemonSets, etc.
We will also discuss the essential role of Labels and Selectors in a microservices-driven architecture as they logically group decoupled objects together.

### Learning Objectives
By the end of this chapter, you should be able to:
- Describe the Kubernetes object model.
- Discuss Kubernetes building blocks, e.g. Nodes, Namespaces, Pods, ReplicaSets, Deployments, DaemonSets.
- Discuss Labels and Selectors.

## Kubernetes Object Model
Kubernetes became popular due to its advanced application lifecycle management capabilities, implemented through a rich object model, representing different persistent entities in the Kubernetes cluster.
Those entities describe:
- What containerized applications we are running.
- The nodes where the containerized applications are deployed.
- Application resource consumption.
- Policies attached to applications, like restart/upgrade policies, fault tolerance, ingress/egress, access control, etc.

With each object, we declare our intent, or the desired state of the object, in the **spec** section. The Kubernetes system manages the **status** section for objects, where it records the actual state of the object.
At any given point in time, the Kubernetes Control Plane tries to match the object's actual state to the object's desired state.
An object definition manifest must include other fields that specify the version of the API we are referencing as the **apiVersion**, the object type as **kind**, and additional data helpful to the cluster or users for accounting purposes - the **metadata**.

Examples of Kubernetes object types are Nodes, Namespaces, Pods, ReplicaSets, Deployments, DaemonSets, etc. We will explore them next.

When creating an object, the object's configuration data section from below the **spec** field has to be submitted to the Kubernetes API Server.
The API request to create an object <mark style="background: #FF5582A6;">must</mark> have the **spec** section, describing the desired state, as well as other details.
Although the API Server accepts object definitions in a JSON format, most often we provide such definition manifests in a YAML format which is converted by **kubectl** in a JSON payload and sent to the API Server.

## Nodes
[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) are virtual identities assigned by Kubernetes to the systems part of the cluster - whether Virtual Machines, bare-metal, Containers, etc. These identities are unique to each system, and are used by the cluster for resources accounting and monitoring purposes, which helps with workload management throughout the cluster.


Each node is managed with the help of two Kubernetes node agents - kubelet and kube-proxy, while it also hosts a container runtime.
The container runtime is required to run all containerized workload on the node - control plane agents and user workloads. 

The kubelet and kube-proxy node agents are responsible for executing all local workload management related tasks - interact with the runtime to run containers, monitor containers and node health, report any issues and node state to the API Server, and managing network traffic to containers.


Based on their pre-determined functions, there are two distinct types of nodes - *control plane* and *worker*.

A typical Kubernetes cluster includes at least one control plane node, but it may include multiple control plane nodes for Highly Available (HA) control plane.

In addition, the cluster includes one or mode worker nodes to provide resource redundancy in the cluster.

There are cases when a single all-in-one cluster is bootstrapped as a single node on a single VM, bare-metal, or Container, when high availability and resource redundancy are not of importance. 
These are hybrid or mixed nodes hosting both control plane agents and user workload on the same system.
Minikube allows us to bootstrap multi-node clusters with distinct, dedicated control plane nodes, however, if our host system has a limited amount of physical resources, we can easily bootstrap a single all-in-one cluster as a single node on a single VM or Container, and still be able to explore most of the topics covered in this course, with the exception of features specific to multi-node clusters, such as DaemonSets, multi node networking, etc.

Node identities are created and assigned during the cluster bootstrapping process by the tool responsible to initialize the cluster agents. 
Minikube is using the default **kubeadm** bootstrapping tool, to initialize the control plane node during the **init** phase and grow the cluster by adding worker or control plane nodes with the **join** phase.

The *control plane nodes* run the control plane agents, such as the API Server, Scheduler, Controller Managers, and etcd in addition to the kubelet and kube-proxy node agents, the container runtime, and add-ons for container networking, monitoring, logging, DNS, etc.

*Worker nodes* run the kubelet and kube-proxy node agents, the container runtime, and add-ons for container networking, monitoring, logging, DNS, etc.

## Namespaces
If multiple users and teams use the same Kubernetes cluster we can partition the cluster into virtual sub-clusters using [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).
The names of the resources/objects created inside a Namespace are unique, but not across Namespaces in the cluster.

To list all the Namespaces, we can run the following command:
`kubectl get namespaces`
![[Pasted image 20240208123009.png]]

Generally, Kubernetes creates four Namespaces out of the box: **kube-system**, **kube-public**, **kube-node-lease**, and **default**.
The **kube-system** Namespace contains the objects created by the Kubernetes system, mostly the control plane agents.
The **default** Namespace contains the objects and resources created by administrators and developers, and objects are assigned to it by default unless another Namespace name is provided by the user.
**kube-public** is a special Namespace, which is unsecured and readable by anyone, used for special purposes such as exposing public (non-sensitive) information about the cluster.
The newest Namespace is **kube-node-lease** which holds node lease objects used for node heartbeat data. 
Good practice, however, is to create additional Namespaces, as desired, to virtualize the cluster and isolate users, developer teams, applications, or tiers:
`kubectl create namespace new-awesome-namespace`
![[Pasted image 20240208123158.png]]

Namespaces are one of the most desired features of Kubernetes, securing its lead against competitors, as it provides a solution to the multi-tenancy requirement of today's enterprise development teams.

[Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) help users limit the overall resources consumed within Namespaces, while [LimitRanges](https://kubernetes.io/docs/concepts/policy/limit-range/) help limit the resources consumed by Containers and their enclosing objects in a Namespace.


## Pods
A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) is the smallest Kubernetes workload object. 
It is the unit of deployment in Kubernetes, which represents a single instance of the application.
A Pod is a logical collection of one or more containers, enclosing and isolating them to ensure that they:
- Are scheduled together on the same host with the Pod.
- Share the same network namespace, meaning that they share a single IP address originally assigned to the Pod.
- Have access to mount the same external storage (volumes) and other common dependencies.

>Single- and Multi-Container Pods
![[Single-_and_Multi-Container_Pods.png]]

Pods are ephemeral in nature, and they do not have the capability to self-heal themselves. 
That is the reason they are used with controllers, or operators (controllers/operators are used interchangeably), which handle Pods' replication, fault tolerance, self-healing, etc.
Examples of controllers are Deployments, ReplicaSets, DaemonSets, Jobs, etc.
When an operator is used to manage an application, the Pod's specification is nested in the controller's definition using the *Pod Template*.

Below is an example of a stand-alone Pod object's definition manifest in **YAML** format, *without* an operator:
```YAML
apiVersion: v1  
kind: Pod  
metadata:  
  name: nginx-pod  
  labels:  
    run: nginx-pod  
spec:  
  containers:  
  - name: nginx  
    image: nginx:1.22.1  
    ports:  
    - containerPort: 80
```

The **apiVersion** field <mark style="background: #FFB86CA6;">must</mark> specify **v1** for the Pod object definition.
The second <mark style="background: #FFB86CA6;">required</mark> field is **kind** specifying the **Pod** object type.
The third required field **metadata**, holds the object's name and optional labels and annotations.
The fourth <mark style="background: #FFB86CA6;">required</mark> field **spec** marks the beginning of the block defining the desired state of the Pod object - also named the **PodSpec**.
Our Pod creates a single container running the **nginx:1.22.1** image pulled from a container image registry, in this case from [Docker Hub](https://hub.docker.com/_/nginx).
The **containerPort** field specifies the container port to be exposed by Kubernetes resources for inter-application access or external client access - to be explored in the Services chapter.
The contents of **spec** are evaluated for scheduling purposes, then the **kubelet** of the selected node becomes responsible for running the container image with the help of the container runtime of the node.
The Pod's name and labels are used for workload accounting purposes.

## DEMO: How to Run Applications with Pods
![[61a5fb9c-6ebc-4d4e-9a16-22481e975246-mp4_720p.mp4]]
https://kubernetes.io/docs/concepts/workloads/pods/

Simple pod YAML file was taken from the documentation above: 
```YAML
apiVersion: v1  
kind: Pod  
metadata:  
  name: nginx    
spec:  
  containers:  
  - name: nginx  
    image: nginx:1.20.2  
    ports:  
    - containerPort: 80
```

![[Pasted image 20240208125900.png]]
Saving the file as `nginx-pod.yaml`

Running the `kubectl apply` command:
```SHELL
kubectl apply -f nginx-pod.yaml
```
![[Pasted image 20240208130105.png]]

We can make sure that the pod has been created by running `kubectl get pods` command:
![[Pasted image 20240208130224.png]]

For a fuller list of details regarding the Pods, we can run `kubectl get pods -o wide`:
![[Pasted image 20240208130336.png]]
We can see that the Pod is ready and running.

###### Method 2:
Instead, we can use the Imperative method of running pods in a cluster:
```SHELL
kubectl run firstrun --image=nginx
```
The first argument, *firstrun*, is the name of the pod.
And the second argument is the option, the image, which is nginx, the latest image of nginx in this case:
![[Pasted image 20240208205132.png]]

Now, running `kubectl get pods -o wide` again in order to make sure that the pod has been created:
![[Pasted image 20240208205303.png]]

Now we have the two pods in the default Namespace.

###### Method 3:
A mix of an imperative method and a YAML definition file.

```SHELL
kubectl run firstrun --image=nginx --port=88 --dry-run=client -o yaml > secondrun.yaml
```

This command reuses the same command we used in the second method, except, this one generates the YAML file for us, `secondrun.yaml`.

That is done with the help of the `--dry-run` option, which will generate a YAML formatted output, a definition manifest for a new pod. 
It will subsequently stored in the file `secondrun.yaml`, in the same folder where we had run the command.

But, since the pod name is the same as the one we had generated in the last method, `firstrun` we will have to change that in this new pod.

Since names are unique in the same Namespace, and both pods being in the same default Namespace, this pod's name will need to be changed.

![[Pasted image 20240208210057.png]]

After changes to the Labels, Pod name and Container name (for the sake of consistency), as well as changing the port to 80, since that is the port than nginx uses, we will now go ahead and run the `kubectl apply` command:
![[Pasted image 20240208210219.png]]

We run `kubectl get pods` in order to list our pods in the cluster:
![[Pasted image 20240208210337.png]]

Now, in case of something going wrong, in order to trouble shoot the pods, we run `kubectl describe pods`.
While it ran fine on my machine, the tutorial does showcase a troubleshooting section which explains the different terminal screenshots.

Once we run the `kubectl describe pods` command, we go ahead and look at the *Events* section in the output displayed by the terminal:
![[Pasted image 20240208210545.png]]
As we can see, the reason for failure of the command is a typo. The author had, on purpose, typed in `nginxx` instead of `nginx` and as a result, Kubernetes did not find the right image to pull.

After the demo, a cleanup is needed. Running the `kubectl delete -f [podname.yaml]` will do the trick:
![[Pasted image 20240208210826.png]]

If we wanted to delete all pods currently running, we can simply run the `kubectl delete pods firstrun secondrun`:
![[Pasted image 20240208211022.png]]

## Labels
[Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) are **key-value pairs** attached to Kubernetes objects (e.g. Pods, ReplicaSets, Nodes, Namespaces, Persistent Volumes).
Labels are used to organize and select a subset of objects, based on the requirements in place.
Many objects can have the same Label(s).
Labels <mark style="background: #FFF3A3A6;">do not</mark> provide uniqueness to objects. Controllers use Labels to logically group together decoupled objects, rather than using objects' names or IDs. (Similar to AWS Tags).

![[Labels2023.png]]

In the image above, we have used two Label keys: **app** and **env**. Based on our requirements, we have given different values to our four Pods. The Label **env=dev** logically selects and groups the top two Pods, while the Label **app=frontend** logically selects and groups the left two Pods. We can select one of the four Pods - bottom left, by selecting two Labels: **app=frontend** **AND** **env=qa**

## Label Selectors
Controllers, or operators, and Services, use [label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) to select a subset of objects. Kubernetes supports two types of Selectors:- **Equality-Based Selectors** 
    Equality-Based Selectors allow filtering of objects based on Label keys and values.
     Matching is achieved using the **=**, **=\=** (equals, used interchangeably), or **!=** (not equals) operators.
      For example, with **env\==dev** or **env=dev** we are selecting the objects where the **env** Label key is set to value **dev**. 
- **Set-Based Selectors**  
    Set-Based Selectors allow filtering of objects based on a set of values.
     We can use **in**, **notin** operators for Label values, and **exist/does not exist** operators for Label keys.
    For example, with **env in (dev,qa)** we are selecting objects where the **env** Label is set to either **dev** or **qa**; with **!app** we select objects with no Label key **app**.

![[Selectors2023.png]]

## ReplicationControllers
Although no longer a recommended controller, a [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) is a complex operator that ensures a specified number of replicas of a Pod is running at any given time, by constantly comparing the actual state with the desired state of the managed application.
If there are more Pods than the desired count, the replication controller randomly terminates the number of Pods exceeding the desired count, and, if there are fewer Pods than the desired count, then the replication controller requests additional Pods to be created until the actual count matches the desired count.
Generally, we do not deploy a Pod independently, as it would not be able to re-start itself if terminated in error because a Pod misses the much desired self-healing feature that Kubernetes otherwise promises.
The recommended method is to use some type of an operator to run and manage Pods.

In addition to replication, the ReplicationController operator also supports application updates. 

However, the default recommended controller is the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) which configures a [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) controller to manage application Pods' lifecycle.

## ReplicaSets
A [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) is, in part, the next-generation ReplicationController, as it implements the replication and self-healing aspects of the ReplicationController.
ReplicaSets support both equality- and set-based Selectors, whereas ReplicationControllers only support equality-based Selectors.

 When a single instance of an application is running there is always the risk of the application instance crashing unexpectedly, or the entire server hosting the application crashing.
If relying only on a single application instance, such a crash could adversely impact other applications, services, or clients. 
To avoid such possible failures, we can run in parallel multiple instances of the application, hence achieving high availability.
The lifecycle of the application defined by a Pod will be overseen by a controller - the ReplicaSet. With the help of the ReplicaSet, we can scale the number of Pods running a specific application container image.
Scaling can be accomplished manually or through the use of an [autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

Below we graphically represent a ReplicaSet, with the replica count set to 3 for a specific Pod template. 
Pod-1, Pod-2, and Pod-3 are identical, running the same application container image, being cloned from the same Pod template.
For now, the current state matches the desired state. 
Keep in mind, however, that although the three Pod replicas are said to be identical - running an instance of the same application, same configuration, they are still distinct in identity - Pod name, IP address, and the Pod object ensures that the application can be individually placed on any worker node of the cluster as a result of the scheduling process.

>*ReplicaSet (Current State Matches the Desired State)
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@ReplicaSet__Current_State_Matches_the_Desired_State_2023.png]]

Below is an example of a ReplicaSet object's definition manifest in YAML format:
```YAML
apiVersion: apps/v1  
kind: ReplicaSet  
metadata:  
  name: frontend  
  labels:  
    app: guestbook  
    tier: frontend  
spec:  
  replicas: 3  
  selector:  
    matchLabels:  
      app: guestbook  
  template:  
    metadata:  
      labels:  
        app: guestbook  
    spec:  
      containers:  
      - name: php-redis  
        image: gcr.io/google_samples/gb-frontend:v3
        ```

Let's continue with the same ReplicaSet example and assume that one of the Pods is forced to unexpectedly terminate (due to insufficient resources, timeout, its hosting node has crashed, etc.), causing the current state to no longer match the desired state.

> *ReplicaSet (Current State and Desired State Are Different)*
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@ReplicaSet__Current_State_and_Desired_State_Are_Different_2023_.png]]

The ReplicaSet detects that the current state is no longer matching the desired state and triggers a request for an additional Pod to be created, thus ensuring that the current state matches the desired state.

>*ReplicaSet (Creating a Pod to Match Current State with Desired State*)
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@ReplicaSet__Creating_a_Pod_to_Match_Current_State_with_Desired_State_2023.png]]

ReplicaSets can be used independently as Pod controllers but they only offer a limited set of features. 
A set of complementary features are provided by <mark style="background: #FFB8EBA6;">Deployments</mark>, the recommended controllers for the orchestration of Pods. 
*Deployments* manage the creation, deletion, and updates of Pods. 
A Deployment automatically creates a ReplicaSet, which then creates a Pod.

Deployment --> ReplicaSet --> Pod created.

There is no need to manage ReplicaSets and Pods separately, the Deployment will manage them on our behalf.

## Deployments
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) objects provide declarative updates to Pods and ReplicaSets. 
The DeploymentController is part of the control plane node's controller manager, and as a controller it also ensures that the current state always matches the desired state of our running containerized application. 
It allows for seamless application updates and rollbacks, known as the default **RollingUpdate** strategy, through **rollouts** and **rollbacks**, and it directly manages its ReplicaSets for application scaling.
It also supports a disruptive, less popular update strategy, known as **Recreate**.

Below is an example of a Deployment object's definition manifest in YAML format:
```YAML
apiVersion: apps/v1  
kind: Deployment  
metadata:
  name: nginx-deployment  
  labels:
    app: nginx-deployment  
spec:  
  replicas: 3  
  selector:  
    matchLabels:
      app: nginx-deployment  
  template:  
    metadata:  
      labels:
        app: nginx-deployment  
    spec:  
      containers:  
      - name: nginx  
        image: nginx:1.20.2  
        ports:  
        - containerPort: 80
```

The **apiVersion** field is the first <mark style="background: #FF5582A6;">required</mark> field, and it specifies the API endpoint on the API server which we want to connect to; it must match an existing version for the object type defined.

The second <mark style="background: #FF5582A6;">required</mark> field is **kind**, specifying the object type - in our case it is **Deployment**, but it can be Pod, ReplicaSet, Namespace, Service, etc. 

The third <mark style="background: #FF5582A6;">required</mark> field **metadata**, holds the object's basic information, such as name, annotations, labels, namespaces, etc.

Our example shows two **spec** fields (**spec** and **spec.template.spec**).
The fourth <mark style="background: #FF5582A6;">required</mark> field **spec** marks the beginning of the block defining the desired state of the Deployment object.
In our example, we are requesting that 3 replicas, that is 3 instances of the Pod, are running at any given time.
The Pods are created using the Pod Template defined in **spec.template**. 
A nested object, such as the Pod being part of a Deployment, retains its **metadata** and **spec** and loses its own **apiVersion** and **kind** - both being replaced by **template**.
In **spec.template.spec**, we define the desired state of the Pod. Our Pod creates a single container running the **nginx:1.20.2** image from [Docker Hub](https://hub.docker.com/_/nginx).

Once the Deployment object is created, the Kubernetes system attaches the **status** field to the object and populates it with all necessary status fields.

In the following example, a new **Deployment** creates **ReplicaSet** **A** which then creates **3 Pods**, with each Pod Template configured to run one **nginx:1.20.2** container image. 
In this case, the **ReplicaSet A** is associated with **nginx:1.20.2** representing a state of the **Deployment**.
This particular state is recorded as **Revision 1**.

>*Deployment (ReplicaSet A Created)
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@Deployment__ReplicaSet_A_Created_2023.png]]

In time, we need to push updates to the application managed by the Deployment object. Let's change the Pods' Template and update the container image from `nginx:1.20.2` to `nginx:1.21.5`. 
The `Deployment` triggers a new `ReplicaSet B` for the new container image versioned `1.21.5` and this association represents a new recorded state of the `Deployment`, `Revision 2`. 
The seamless transition between the two ReplicaSets, from `ReplicaSet A` with three Pods versioned `1.20.2` to the new `ReplicaSet B` with three new Pods versioned `1.21.5`, or from `Revision 1` to `Revision 2`, is a <mark style="background: #D2B3FFA6;">Deployment rolling update.</mark>

A **rolling update** is triggered when we update specific properties of the Pod Template for a deployment. 
While planned changes such as updating the container image, container port, volumes, and mounts would trigger a new Revision, other operations that are dynamic in nature, like scaling or labeling the deployment, do not trigger a rolling update, thus do not change the Revision number.

Once the rolling update has completed, the **Deployment** will show both **ReplicaSets A** and **B**, where **A** is scaled to 0 (zero) Pods, and **B** is scaled to 3 Pods. This is how the Deployment records its prior state configuration settings, as **Revisions**.

> *Deployment (ReplicaSet B Created*
![[asset-v1 LinuxFoundationX+LFS158x+1T2022+type@asset+block@Deployment__ReplicaSet_B_Created_.png]]

Once **ReplicaSet B** and its **3 Pods** versioned **1.21.5** are ready, the **Deployment** starts actively managing them. 
However, the Deployment keeps its prior configuration states saved as Revisions which play a key factor in the **rollback** capability of the Deployment - returning to a prior known configuration state. 
In our example, if the performance of the new **nginx:1.21.5** is not satisfactory, the Deployment can be rolled back to a prior Revision, in this case from **Revision 2** back to **Revision 1** running **nginx:1.20.2** once again.

>*Deployment Points to ReplicaSet B
![[Deployment_Points_to_ReplicaSet_B.png]]


## DEMO: Deployment Rolling Update and Rollback
![[LinuxFoundationXLFS158x-V000800_DTH.mp4]]

We start out by creating a new *Deployment* called `mynginx`, which is going to run pods that run containers running the image `nginx:1.15-alpine`.

```SHELL
kubectl create deployment mynginx --image=nginx:1.15-alpine
```

![[Pasted image 20240210212738.png]]

Then, we want to display all the ReplicaSets and Pods that that are labeled as `app=mynginx`:

```SHELL
kubectl get deploy,rs,po -l app=mynginx
```
![[Pasted image 20240210213057.png]]

As we can see, the terminal only displays `mynginx` Deployment, the ReplicaSets associated with this Deployment, and the only Pod that was created with this Deployment.

We can see that everything has the Ready status.

Now, we scale the Deployment up to 3 replicas:
```SHELL
kubectl scale deploy mynginx --replicas=3
```
![[Pasted image 20240210213421.png]]

Now, we list the Deployments again by running the following command once again:
```SHELL
kubectl get deploy,rs,po -l app=mynginx
```
![[Pasted image 20240210213508.png]]
As we can see, we now have three running Pods, three Replicas and the Deployment is ready.

Now, for reference, we will be remembering the name of the ReplicaSet of *mynginx*: `7fbcf7bbfd` to see how this state is recorded.

With our ReplicaSet being `7fbcf7bbfd`, it will undergo several changes throughout the rolling update and rollback processes.

Now, we are going to run the following command:
```SHELL
kubectl describe deploy mynginx
```
![[Pasted image 20240211155122.png]]
We will be looking out for the Image. (We can also run `kubectl describe deployment`).

As we can see, the image is currently *nginx:1.15-alpine*.

Running `kubectl rollout history deploy mynginx` command will show us the rollout history (We can also run `kubectl rollout history deployment`):
![[Pasted image 20240211155512.png]]

So far, we only have a single Revision.
*Revision 1* is associated with the `nginx:1.115-alpine` image with the `7fbcf7bbfd` ID.

We can run `kubectl rollout history deploy mynginx --revision=1` in order to display further details about the specific Revision:
![[Pasted image 20240211155733.png]]

> *Rolling updates do not necessarily mean an Upgrade. We can perform a Rolling Update while moving down in the image version.*

Now, we are going to be upgrading our image via a Rolling update:
```SHELL
kubectl set image deployment mynginx nginx=nginx:1.16-alpine
```
![[Pasted image 20240211160117.png]]

Now, we will look at the Rollout history of deployment once again:
![[Pasted image 20240211160234.png]]
We can see that now we have a new Revision: 1 and 2, with 2 being the most recent Revision.

Running `kubectl rollout history deploy mynginx --revision=1` in order to showcase the difference between the two Revisions:
![[Pasted image 20240211160414.png]]
*The nginx has an image version of 1.15-alpine*

![[Pasted image 20240211160506.png]]
*The nginx has an image version of 1.16-alpine*

Now, we will be displaying our application objects with the following command that we had ran previously:
`kubectl get deploy,rs,po -l app=mynginx`
![[Pasted image 20240211160732.png]]

We can see that we have the same Deployment: 3 replicas, ready.
The three pods, running.

However, if we look at the ReplicaSets, we will see the original ReplicaSet that we had originally set up, `7fbcf7bbfd`, with the three Replicas, has now been scaled down to zero. 

So the `7fbcf7bbfd` ReplicaSet is recorded as the original state, and we can rollback to that state any time we want.

The new ReplicaSet, `6fdbc5d54c`, is associated with the new and current *1.16-alpine* image.
It is also associated with the Revision number two.

Now, in case we are not happy with the new rollout update, we can always rollout back to the previous Revision 1.
And to do that, we run:
`kubectl rollout undo deployment mynginx --to-revision=1`
![[Pasted image 20240211164816.png]]

We run `kubectl rollout history deploy mynginx` once again to take a look at the Rollout history.
![[Pasted image 20240211202259.png]]
Revision 1, which was the original Revision has now become Revision 3, which is the most recent and the current Revision

Revision 2 is still associated with the *1.16-alpine nginx*, and Revision 3 is associated with the rolled back version *1.15-alpine*.

Now, if we try to check Revision 1 in the Deploy history, we get the following error:
![[Pasted image 20240211202647.png]]
Because Revision 1 just became Revision 3.

Now, lets take a look at our deployment, ReplicaSets and Pods:
`kubectl get deployment,rs,po -l app=mynginx`
![[Pasted image 20240211202830.png]]
We can see that the original ReplicaSet `7fbcf7bbfd` has been scaled back up to three replicas.

And the other ReplicaSet, with the *1.16-alpine*version, also associated with Revision 2, has now been scaled down to zero.

The state has been recorded in the ReplicaSet, and we can always rollback to that Revision if we wanted to.

By default, we can perform up to 10 consecutive rolling updates.
As well as then rollback to any one of those 10 recorded states.

In this case we just performed one rolling update and one roll back.

Rolling updates and roll backs are not Deployments exclusive. They are supported by other controllers as well, such as DaemonSets and StatefulSets.


## DaemonSets
[DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) are operators designed to manage node agents. 
They resemble ReplicaSet and Deployment operators when managing multiple Pod replicas and application updates, but the DaemonSets present a distinct feature that enforces a single Pod replica to be placed per Node, on all the Nodes. 
In contrast, the ReplicaSet and Deployment operators by default have no control over the scheduling and placement of multiple Pod replicas on the same Node.

DaemonSet operators are commonly used in cases when we need to collect monitoring data from all Nodes, or to run a storage, networking, or proxy daemons on all Nodes, to ensure that we have a specific type of Pod running on all Nodes at all times. 
They are critical API resources in multi-node Kubernetes clusters. 
The kube-proxy agent running as a Pod on every single node in the cluster, or the Calico networking node agent implementing the Pod networking across all nodes of the cluster, are both examples of applications managed by DaemonSet operators.


Flutter
IOS ANDROID WEB

REACT
.NET 6/7

Study the company
know everything about the company

Mention everything i know about the company

Something i made even if small 

I heard about it but i know that other platform better and etc. etc. 

Thinking out loud V IMPORTANT 
Do you mean this one or that one 
Get to the solution through a conversation 

Know the CEO 

Know the AZURE concepts and 


REDIS
SQL
