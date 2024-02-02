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

