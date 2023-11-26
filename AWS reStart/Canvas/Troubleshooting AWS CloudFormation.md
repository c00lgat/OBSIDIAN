https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html
The link above is a good starting point for CloudFormation troubleshooting. 


If CloudFormation fails to create, update or delete your stack, we can see the error messages or logs to help us identify the issue.
Such errors can be found in the AWS CloudFormation console.
If an error occurred on an EC2 instance, we can log in to that instance and examine the `cloud-init` and `cfn` log files.


###### Troubleshooting templates
It is a common practice to store CloudFormation templates that we build on an S3 bucket.
We can specify the S3 bucket location while choosing a template to run a specific template that we want to run as a stack.
You have to make sure that you have the right permissions to access the bucket, as well as that the bucket does exist and the location is valid.
![[Pasted image 20231126095130.png]]


###### Troubleshooting resources
`Resources fail to create`
Things to consider:
- Does the user have the permissions to create the corresponding AWS resource?
- Does the resource type have all required parameters?
	- Compare your code against working templates.
	- Check the documented syntax for the resource in the AWS CloudFormation User Guide.
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html


If you attempt to create an AWS CloudFormation stack from a template and you see an error message that one of the resources failed to create, you can investigate the following areas.

First, does the user have the permissions to create that type of resource? Check the AWS Identity and Access Management (IAM) policy permissions. Check the user’s level of access for the AWS service that the resource is a part of.

Second, verify that the specified resource type has all the required parameters. The easiest way to do this is to review the JavaScript Object Notation (JSON) or YAML Ain’t Markup Language (YAML) code section in the template where you specify the resource. Then, compare that code against other code that creates the same type of resource, and is also known to work.


###### Troubleshooting a WaitCondition
`WaitCondition failure`
If WaitCondition times our or returns an error, your `CloudFormation::Init` code has an error.
- Analyze the `cfn-init.log` and `cfn-wire.log` files for details.
- Collect logs through Amazon CloudWatch logs.
- Set `--on-failure DO_NOTHING` to keep the instance from rolling back so that you can log in and examine the logs.
- Most common error:
	- URLs for references resources-such as scripts, MSI files (Microsoft installer files)m and others- return HTTP 403 or 404 errors.

Recall that WaitConditions are often used when an EC2 instance resource is created. If a WaitCondition times out or returns an error when you attempt to create your AWS CloudFormation stack, it means your CloudFormation::Init code has an error.

If the EC2 instance is still accessible after you notice the error, analyze the cfn-init.log and the cfn-wire.log files for details. You can configure Amazon CloudWatch Logs to collect the logs from the instance.

You could also try running the create stack-command again. However, this time, specify --on-failure DO_NOTHING to keep instance from rolling back so that you can log in to the instance and examine the logs.

The most common error occurs when files that the CloudFormation::Init code references for resources—such as scripts, MSI files (Microsoft Installer files), and others—return HTTP 403 or 404 errors. These errors means that the referenced resources cannot be accessed from the instance.


###### AWS CloudFormation errors
`Troubleshooting resources`
- Template and resource-creation errors are returns in the <mark style="background: #D2B3FFA6;">AWS CloudFormation console</mark> and on <mark style="background: #D2B3FFA6;">stdout</mark>. 
- User data and `CloudFormation::Init` errors are written to the error logs <mark style="background: #FF5582A6;">cloud-init.log</mark>, <mark style="background: #FF5582A6;">cfn-init.log</mark>, and <mark style="background: #FF5582A6;">cfn-wire.log</mark> located at:
	- Linux: /var/log
	- Microsoft Windows: C:\\cfn\
- Options for retrieving
	- Log in to the instance
	- Use CloudWatch Logs to automatically upload logs

If AWS CloudFormation fails to create, update, or delete your stack, you can view error messages or logs to help you learn more about the issue.

This slide describes general methods for troubleshooting an AWS CloudFormation issue.

Template and resource-creation errors are returned in the AWS CloudFormation console and on stdout. For example, in the AWS CloudFormation console, you can view the status of your stack. You can view a list of stack events while your stack is being created, updated, or deleted.

If an error occurs when the stack runs, you can find the stack event that failed in this view. You can then expand the details to learn information about what caused the error for that event. The status reason might contain an error message from AWS CloudFormation or from a particular service. These error messages can help you troubleshoot your problem.

For Amazon EC2 issues, connect to the instance—if you can—and review the cloud-init and cfn logs. These logs are published on the EC2 instance. In Linux instances, they are in the /var/log/ directory. In Microsoft Windows instances, they are in the C:\cfn directory. These logs capture processes and command outputs while AWS CloudFormation sets up your instance. For Windows, you can also access the EC2Configure service and cfn logs in the `%ProgramFiles%\Amazon\EC2ConfigService` and `C:\cfn\log` directories. You can also configure your AWS CloudFormation template so that the logs are published to Amazon CloudWatch. CloudWatch displays logs in the AWS Management Console, so you do not need to connect to your EC2 instance.



Some key takeaways from this module:
• If AWS CloudFormation fails to create, update, or delete your stack, you can view error messages or logs to help you learn more about the issue.
• It is a common practice to store AWS CloudFormation templates on Amazon S3. You then specify the Amazon S3 location when you choose a template so that you can run a stack.
• If a WaitCondition times out or returns an error when you attempt to create your AWS CloudFormation stack, your CloudFormation::Init code has an error.


