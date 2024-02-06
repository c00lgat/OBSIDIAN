https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/home

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

### Advanced Minikube Features (1)

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

