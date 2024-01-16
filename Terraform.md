https://youtu.be/7xngnjfIlK4?si=QIzK6oF260JFzrZK
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

- Declarative: define the end state of what we want: 5 servers, one load balancer, an S3 bucket and then the tool manages what API calls need to be made and how to actually make it happen
- Imperative: tell the system what we want to happen and the sequence in which we want them to happen.
> A lot of these tools fall more on the imperative side; some do offer capabilities that make the tools more declarative and make those scripts idempotent so that they can be ran multiple times.

Terraform is more on the declarative side of tools. We specify the end state that we want our infrastructure to take, and then the tools handles the details of how to get there.


---
# Terraform Overview + Setup
- Terraform is a tool for building, changing and versioning infrastructure safely and efficiently.
- Enables application software best practices to infrastructure.
- Compatible with many clouds and services - cloud agnostic. Can interact with anything with an API.

## Common Patterns:
`Terraform` is usually used along with `Ansible`. 
With `Terraform` handling the provisioning; spinning up virtual servers for example, and `Ansible` handling the configuration management side; install all the necessary dependencies on said resources such as virtual servers.
Like we could provision a virtual server that is running Ubuntu and install all the necessary dependencies needed for our application and we can use `Ansible` for that.

---
## Basic Usage Sequence:
- terraform init
- terraform plan
- terraform apply
- terraform destroy

`Terraform Core` is the engine that parses the configuration from the `Terraform State` file and providers, mapping what's needed from the core to the cloud providers themselves.

When the `init` command, the associated providers that were defined the `terraform block` in our code base are then downloaded. It gets the code for the `AWS Provider` from the `terraform registry`; downloads it and puts it in our working directory.
After the `init` command is ran, a new folder is created in our working directory, called `.terraform` (a hidden directory). Inside it is the official registry information needed.
![[Pasted image 20240115205344.png]]

We are also greeted with a new file aside from the new directory, the lock file. `.terraform.lock.hcl` contains information about the specific dependencies and providers that are installed within the workspace. 

If terraform modules are used, they too will appear under the `.terraform/modules/` directory in our working directory.
![[Pasted image 20240115205551.png]]

---

### State File
Terraform's representation of the world.
JSON file containing information about every resources and data object that we have deployed using terraform.
![[Pasted image 20240115205731.png]]
It gives us information about all the resources we've deployed.

<mark style="background: #FF5582A6;">The State File contains sensitive information (database password for example)</mark>
Therefore, the State File needs to be protected accordingly, making sure that it is encrypted and permissions are set to the correct set of individuals that would have access to it.

The State File can be stored locally or remotely:
1. Local Backend; the state file is stored on our local machine. 
	1. <mark style="background: #BBFABBA6;">Convenient and easy to get started. </mark>
	2. <mark style="background: #FF5582A6;">Not recommended, as it will have sensitive values in plain text.</mark>
	3. <mark style="background: #FF5582A6;">Uncollaborative; makes it harder to work on the infrastructure by other individuals that need access to it.</mark>
	4. <mark style="background: #FF5582A6;">Very Manual: every time we are interacting with the configuration; we need to manually run terraform apply command within the terminal each time. Ideally we need to automate that. </mark>
2. With a remote backend, having the state file stored remotely on a server somewhere. 
	1. One option is using `Terraform Cloud` which is a managed service that will host our state file for us and will manage permissions for us etc.
	2. Self managed remote backend to store those state files such as amazon S3.
	- <mark style="background: #BBFABBA6;">Sensitive data is encrypted.</mark>
	- <mark style="background: #BBFABBA6;">Collaboration possible.</mark>
	- <mark style="background: #BBFABBA6;">Automation possible. No longer dependent on running the commands locally on our machine, we can instead run things like `github actions` or other automation pipelines that can interact with the remote file state.</mark>
	- <mark style="background: #FF5582A6;">Increased complexity.
</mark>

---
### $ terraform plan 
`terraform plan` command takes the `Terraform Config` file <mark style="background: #ADCCFFA6;">(Desired State)</mark> which is defined on our system; what we want the infrastructure to look like.
The `terraform plan` command then compares the `Terraform Config` file to the `Terraform State` <mark style="background: #ADCCFFA6;">(Actual State)</mark> which is the actual state of the world (the resources that are currently running in the cloud).

As long as no config changes were made through the GUI or through any other means that is not through Terraform, `Terraform State` should represent the actual state of the world.

> Making changes to the infrastructure outside of the terraform workflow should be avoided.

---
### $ terraform destroy
We run this command when we want to clean up at the end of the project; it is never ran for a live project that is still executing.

---
## Remote Backend (Terraform Cloud)
![[Pasted image 20240116201042.png]]

## Remote Backend (AWS)
![[Pasted image 20240116201132.png]]

Instead of using `Terraform Cloud`, one could use an AWS managed service instead for the terraform config file. 
To do so; an `S3 bucket` used for storage is needed, as well as a `DynamoDB` table which is used for locking.
The `S3 bucket` is where the `state file` will live and we can tell it whether we want it to be encrypted or not; obviously it is a best practice to have it encrypted.

As for the `DynamoDB table`, we need to have the setting `terraform-state-locking` for it. And that is because, it is possible that we will have multiple people working on the same project at once; we want to prevent having different people trying to apply different changes at the same time. And in order to solve that, we can leverage the atomic guarantees that DynamoDB offers so that if we issue a command, we can lock the terraform configuration such as that if someone else issues any commands during the same time, they will be rejected until our command is finished.

Now, how will we be able to provision these S3 bucket and DynamoDB tables given that we want to provision everything with infrastructure's code but we don't have these resources provisioned yet. 

And for that, we have to first provision these resources with the default local backend. 
And once that is done, we can simply import them into our configuration.

```HCL
terraform {
	required_providers {
		aws = {
			source = "hashicorp/aws"
			version = "~> 5.0"
		}
	}
}

provider "aws" {
	region = "us-west-2"
}

resource "aws_s3_bucket" "terraform_state" {
bucket = "devops-directive-tf-state"
force_destroy = true
versioning {
	enabled = true
}

server_side_encryption_configuration {
	rule {
	apply_server_side_encryption_by_default{
			sse_algorithm = "AES256"
		}
	}
}
}

resource "aws_dynamodb_table" "terraform_locks" {
	name = "terraform-state-locking"
	billing_mode = "PAY_PER_REQUEST"
	hash_key = "LockID"
	attribute {
		name = "LockID"
		type = "S"
	}
}
```
 > It is important that the hash_key = "LockID" which is a key attribute in order for it to work as intended.

Once our configuration has been set up that way, we run the `terraform apply` which is the normal process