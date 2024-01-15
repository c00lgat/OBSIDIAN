### Evolution of Cloud + Infrastructure as Code
- Infrastructure provisioned via APIs
- Servers created and destroyed in seconds
- Long-lived + mutable -> Short-lived + immutable
	- Rather than having a server that is up for years on end and is being modified, different dependencies are being installed and changed and patched. 
	- Nowadays, when a server needs to be modified, we can just spin up a brand new server with those dependencies already installed.
	- So every server in the cloud now is usually short-lived immutable thing that we are never gonna change. 
	- Paradigm shift.

### Provisioning Cloud Resources:
# GUI
![[Pasted image 20240115123359.png]]

# API/CLI
![[Pasted image 20240115123414.png]]
# IaC
![[Pasted image 20240115123434.png]]`IaC` enables you to take your entire infrastructure and define it in the code base. 
It lets us know what is exactly positioned at any given time.
Provisioning multiple environment makes it harder to do so using the GUI, so defining things as code as configurations within the code base, we have much higher confidence telling what we have actually deployed, and use the power of programming languages to have multiple copies of the same thing and have confidence that they are deployed identically.

### Categories of IaC tools:
1. `Ad hoc scripts`: `shell script` that makes some API calls to amazon that says provision me five EC2 instances. Is that really infrastructure as code? Borderline. Although it does count towards code within the code base that provisions AWS resources. 
2. `Configuration management tools`: `ansible`, `puppet` and `chef`; they are positioned to manage the software that is running and the configuration of the infrastructure, more suited towards on-premises setups where you're provisioning some hardware and there is the need to manage what software is installed and how it is configured.
3. `Server Templating tools`: building out a template for what we are going to provision onto a server, similarly to AMI. Any image that is provisioned from a template, and we can build all dependencies through that template. 
4. `Orchestration tools`: for orchestration containers; how you can define your application deployment, how we can take the code and deploy it in a certain way onto whatever system we have provisioned in the background
5. `Provisioning tools`: focuses on provisioning the cloud resources that we have running on the cloud.
	1. Declarative: define the end state of what we want: 5 servers, one load balancer, an S3 bucket and then the tool manages what API calls need to be made and how to actually make it happen
	2. Imperative:: 


