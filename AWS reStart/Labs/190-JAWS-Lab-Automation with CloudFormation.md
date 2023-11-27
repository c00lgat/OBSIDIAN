Deploying infrastructure in a consistent, reliable manner is difficult — it requires people to follow documented procedures without taking any undocumented shortcuts. Plus, it can be difficult to deploy infrastructure out-of-hours when less staff are available. AWS CloudFormation changes this by defining infrastructure in a template that can be automatically deployed — even on an automated schedule.

This lab provides experience in deploying and editing CloudFormation stacks. It is an interactive experience, requiring you to consult documentation to discover how to define resources within a CloudFormation template.

The lab will demonstrate how to:
- **Deploy** an AWS CloudFormation stack with a defined Virtual Private Cloud (VPC), and Security Group.
- **Configure** an AWS CloudFormation stack with resources, such as an Amazon Simple Storage Solution (S3) bucket and Amazon Elastic Compute Cloud (EC2).
- **Terminate** an AWS CloudFormation and its respective resources.

You will begin by deploying a CloudFormation stack that creates a VPC as shown in this diagram:
![[initial-template.png]]

![[task1.yaml]]
