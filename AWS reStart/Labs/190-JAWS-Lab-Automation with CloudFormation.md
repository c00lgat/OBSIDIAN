Deploying infrastructure in a consistent, reliable manner is difficult — it requires people to follow documented procedures without taking any undocumented shortcuts. Plus, it can be difficult to deploy infrastructure out-of-hours when less staff are available. AWS CloudFormation changes this by defining infrastructure in a template that can be automatically deployed — even on an automated schedule.

This lab provides experience in deploying and editing CloudFormation stacks. It is an interactive experience, requiring you to consult documentation to discover how to define resources within a CloudFormation template.

The lab will demonstrate how to:
- **Deploy** an AWS CloudFormation stack with a defined Virtual Private Cloud (VPC), and Security Group.
- **Configure** an AWS CloudFormation stack with resources, such as an Amazon Simple Storage Solution (S3) bucket and Amazon Elastic Compute Cloud (EC2).
- **Terminate** an AWS CloudFormation and its respective resources.

You will begin by deploying a CloudFormation stack that creates a VPC as shown in this diagram:
![[initial-template.png]]


![[task1.yaml]]
You will begin by deploying a CloudFormation stack that creates a VPC as shown in this diagram:
- The [Parameters section](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) is used to prompt for inputs that can be used elsewhere in the template. The template is asking for two IP address (CIDR) ranges for defining the VPC.
- The [Resources section](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) is used to define the infrastructure to be deployed. The template is defining the VPC, and a Security Group.
- The [Outputs section](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) is used to provide selective information about resources in the stack. The template is providing the Default Security Group for the VPC that is created.

The template is written in a format called [YAML](https://en.wikipedia.org/wiki/YAML), which is commonly used for configuration files. The format of the file is important, including the indents and hyphens. CloudFormation templates can also be written in JSON.

With the YAML file downloaded, we can start creating our stack.
We go to the CloudFormation AWS Console page, click `Create stack`, upload the template file, give the stack a name and proceed with the default settings.

Once submitted, we should see the stack entering the __CREATE_IN_PROGRESS__ status.

The listing in the **Events** tab shows (in reverse order) the activities performed by CloudFormation, such as starting to create a resource and then completing the resource creation. Any errors encountered during the creation of the stack will be listed in this tab.

The **Resources** tab shows the resources that are being created. CloudFormation determines the optimal order for resources to be created, such as creating the VPC before the subnet.

