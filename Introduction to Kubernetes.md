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


