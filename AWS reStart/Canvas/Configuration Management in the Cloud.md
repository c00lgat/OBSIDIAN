This lesson explores the benefits of configuration management in the cloud. It identifies AWS services that you can use to implement configuration management strategies.

In this lesson, you will learn how to:
• Describe the benefits of configuration management 

• Identify key AWS services for configuration management 

• Create a configuration management strategy



The many benefits of configuration management:
- Increase efficiency 
- Validate every change before release
- Reduce cost by removing unwanted resources
- Enforce security at every layer
- Deploy configuration changes to running instances
- Make configuration automated and repeatable


The manual configuration of distributed systems is time-consuming and error-prone, and it can lead to inconsistently configured systems. Therefore, the ability to automate, monitor, and track configuration changes is a key component of any configuration management solution.

Configuration management provides many benefits. One of the key benefits is that it enables you to launch new resources quickly and consistently in an automated or semiautomated way. It is commonly used for deploying configuration changes to running instances with increased consistency and limited server downtime

Some of the managed services and tools from AWS that customers commonly use for configuration management include AWS CloudFormation and AWS OpsWorks. The Amazon CloudWatch service complements these services by providing a monitoring service that can trigger actions when changes to your resources occur.

![[Pasted image 20231125154655.png]]

Many AWS customers use configuration tools to launch new EC2 instances and other resources in an automated, repeatable manner. The flexibility of the configuration management tools enables the implementation of a complete configuration management strategy.

The diagram illustrates one way in which configuration software can be integrated within an AWS architecture. Assume that you wanted to use configuration software to initialize a set of Amazon EC2 instances as web servers. The scenario details are as follows:
1. `An administrator configures a configuration server.`
	This is usually a standalone Amazon EC2 instance. The instance will host a set of templates, which describe all the applications, files, and configurations necessary to launch AWS resources. 
	
	For example, a web server template might specify how to automate the launch of an EC2 instance.
	The web server template might then specify the following for web server content: 
	 - Installation of HTTP
	 - Configuration of the web server httpd.conf file 
	 - Installation of all necessary programming language environments (such as PHP or Ruby)
	 - Creation of a directory and file structure on the EC2 instance
	 
	 The configuration server would probably contain a number of recipes for configuring dozens of different types of servers. Examples of servers include MySQL server, NAT server, Windows IIS server, Maven repository, and so on.

2. Administrator creates the configuration templates. Then, the administrator publishes them to the configuration server and checks them into a source control system for version management and change tracking.
   
3. Administrator might use any combination of custom scripting, AWS CloudFormation, AWS OpsWorks, or other similar products to describe and create AWS Cloud deployments. 

These deployments might consist of Amazon EC2 instances, virtual private cloud (VPC) configurations, databases, and other required AWS resources.


AWS provides a number of technologies for configuring and deploying your Amazon EC2 instances and other AWS infrastructure. This module will explore some of these technologies. It will also discuss approaches for combining these technologies into a comprehensive configuration and deployment strategy. Available features and resources include:
- User data – Enables you to author scripts that are run on instance launch. The use of scripts is one of the simplest approaches to configuration management. However, at the enterprise level, it becomes more difficult to manage and version infrastructure by only using scripts.
  
- Amazon Machine Images (AMIs) – By creating base images that are customized to the needs of your organization, you can pre-deploy installations and configurations into the EC2 instances that are launched from the AMI. By using this configuration method, you can potentially reduce deployment times.
  
- Configuration and deployment frameworks – Technologies such as Chef, Puppet, and Ansible enable you to configure new instances by using templates. You can update configurations dynamically in response to change.
  
- AWS OpsWorks – A configuration management service that provides managed instances of Chef and Puppet.
  
- AWS CloudFormation – An AWS service that enables you to configure architectures for repeatable deployments.


#### Using configuration software
###### Benefits of using a configuration server
- Can greatly simplify common administrative tasks.
- Offers a configuration that is idempotent.
	- Resources are allocated only once
	- Manual changes are detected and rolled back
- Supply user data to instance to kick off client configuration
	- Install client and any required configuration and security credentials
	- Specify the templates to be run

Using a configuration server can simplify many common administrative tasks. The most common example is provisioning and de-provisioning user access to Amazon EC2 instances.

`Simplified common tasks`
Suppose that Jane, an engineer, was granted access to multiple Amazon EC2 instances across the fleet. That is, Jane has a private key that enables her to log in with her unique user ID and perform administrative tasks on these instances. What happens when Jane leaves the company? Without a configuration server, de-provisioning Jane's access to these servers can be a manual nightmare. However, by using a configuration server, a systems administrator can easily change Jane's status in the system. The administrator can then apply this change to all instances in the fleet with a few simple commands.

`Idempotent configuration`
One of the advantages of using a configuration server (such as Chef, Puppet, or Ansible) is that configuration is idempotent. Repeating commands and functions do not alter the surrounding system or environment. Resources that are created or configured by a configuration server are configured or created only once. If manual modifications are made to the configuration of an instance, the configuration server detects them and rolls them back. This ensures that the integrity of the instance isn't compromised by an accidental change. You will see an example of this process in the Chef-Solo demonstration.

