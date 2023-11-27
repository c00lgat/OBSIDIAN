###### Lab - Managing Resources with Tagging

This lab is divided into two parts:
- In the **Task** portion of this lab, you will use the AWS Command Line Interface (CLI) to inspect the tags assigned to a number of Amazon EC2 instances. You will then use pre-provided scripts to shut down and start up a number of Amazon EC2 instances simultaneously, based on their tags.
- In the **Challenge** portion of this lab, you will be challenged to think of a way to terminate instances that fail to implement specific tags.

**Objectives** After completing this lab, you will be able to:
- Apply tags to existing AWS resources.
- Find resources based on tags.
- Use the AWS CLI or AWS SDK for PHP to stop and terminate Amazon EC2 instances based on certain attributes of the resource.

The environment for this lab (pictured below) consists of:
- Amazon VPC named Lab VPC
- Public subnet
- Private subnet
- Amazon EC2 Linux instance named CommandHost AWS Command Line Interface (CLI) tools have been pre-installed and configured for you on this instance
- 8 Amazon EC2 Linux instances
- Private instances have three custom tags applied to them:

| Tag Name    | Content                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Project     | The project that the instance belongs to. The instances in this lab belong to one of two projects: ERPSystem and Experiment1. |
| Version     | The version of the project that this instance belongs to. All Version tags are currently set to 1.0.                          |
| Environment | One of three values: development, staging, or production.                                                                     |


In the Task portion of this lab, you will log in to the Command Host and run some commands to find and change the Version tag on all development instances. You will run several examples that show how you can use the JMESPath syntax supported by the AWS CLI `--query` option to return richly formatted output. You will then use a set of pre-provided scripts to stop and re-start all instances that are tagged as belonging to the **development** environment.

![[Pasted image 20231126211108.png]]

First, we log into the Command host EC2.
And we are going to be using the AWS CLI in order to find the resources in the private subnet that belong to the `ERPSystem` project and are in the Environment named `development`.

To find all instances in the account that are tagged with a tag of `Project` and a value of `ERPSystem`, run the following command:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
```

The command outputs the full set of parameters available for all seven instances that are tagged `Project=ERPSystem`. Next we will use the `--query` option to narrow down the results.


Using the `--query` parameter to limit the output of the previous command to only the instance ID of the discovered instance:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].InstanceId'
```
![[Pasted image 20231126212315.png]]

The `--query` command used in this example uses the `JMESPath` wildcard syntax to specify that the command should iterate through all reservations and all instances and return the InstanceId for each instance in the return results.

This is an improvement over returning every property of our instances. 
But what if we wanted to include multiple fields in the output?

The following command will include both the instance ID and the Availability Zone of each instance in the return result:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```
![[Pasted image 20231126212546.png]]

As seen in the previous command, we can specify an alias for each property in order to return a more abbreviated output format.

But there is still one missing key information. The instance names.

To include the value of `Project` tag in your output, run the following command:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value}'
```
![[Pasted image 20231126212838.png]]
The value of a specific named tag can be retrieved via a JMESPath query, using the following syntax:
```bash
Tags[?Key==\`Project\`] | [0].Value
```
The syntax instructs the JMESPath to find all elements within the **Tags** array that have a **Key** value of **Project**. The output of that command is then piped to another command that selects the first instance of this filtered set and selects the named parameter **Value**, which is the value of the **Project** tag. This result is then assigned the alias **Project**.

The following command will include the **Environment** and **Version** tags in the output:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```
![[Pasted image 20231126213226.png]]

###### Changing version Tag for Development Process
We will change all of the **Version** tags on the instances marked as **development** for the project **ERPSystem**.

```bash
#!/bin/bash

ids=$(aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" --query 'Reservations[*].Instances[*].InstanceId' --output text)

aws ec2 create-tags --resources $ids --tags 'Key=Version,Value=1.1'
```
This script first uses the command `aws ec2 describe-instances` to return only a list of instance IDs for the development machines that belong to the **ERPSystem** project. It then passes those values to the `aws ec2 create-tags` command, which either creates a new tag or (in this case) overwrites an existing tag.

> Notice how the first command uses the **--output text** option to manipulate the return results as text instead of as JSON. Using this command instead of JSON on a simple return result—in this case, a list of IDs—can make it easier to manipulate the return result and pass it to other commands.

We run the command, and then make sure that the right instances have been changed, and the ones not belonging to **ERPSystem** were not affected by running the following command:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId, AZ:Placement.AvailabilityZone, Project:Tags[?Key==`Project`] |[0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```
![[Pasted image 20231126213731.png]]


