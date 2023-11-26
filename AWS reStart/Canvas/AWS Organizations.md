In this lesson, you will learn how the AWS Organizations service provides billing and support functions. You will also review the main features and benefits of AWS Organizations.

![[Pasted image 20231126103755.png]]

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations include consolidated billing and account management capabilities that help you to better meet the budgetary, security, and compliance needs of your business.

The diagram shows a basic organization, or root. This example organization consists of seven accounts that are organized into six organizational units (OUs). An OU is a container for accounts within a root. An OU can also contain other OUs, which enables you to create a hierarchy that looks like an upside-down tree. The tree has a root at the top and branches of OUs that reach down, ending in accounts that are the leaves of the tree.

When you attach a policy to one of the nodes in the hierarchy, it flows down and affects all the branches and leaves. This organization has several policies that are attached to some of the OUs or directly to accounts.

An OU can have only one parent and, currently, each account can be a member of exactly one OU. An account is a standard AWS account that contains your AWS resources. You can attach a policy to an account to apply controls to only that one account.

![[Pasted image 20231126104045.png]]

The main benefit of AWS Organizations are:
- Centrally managed access policies across multiple AWS accounts.
- Controlled access to AWS services. 
- Automated AWS account creation and management. 
- Consolidated billing across multiple AWS accounts.


###### Security with AWS Organizations
AWS Organizations does not replace associating AWS Identity and Access Management (IAM) policies with users, groups, and roles within an AWS account.

IAM policies enable you to allow or deny access to AWS services—such as Amazon Simple Storage Service (Amazon S3)—and individual AWS resources (like a specific S3 bucket) or individual application programming interface (API) operations (like s3:CreateBucket). An IAM policy can be applied only to IAM users, groups, or roles, and it can never restrict the AWS account root user.

In contrast, with Organizations, you use service control policies (SCPs) to allow or deny access to particular AWS services for individual AWS accounts, or for groups of accounts in an organizational unit (OU). The specified actions from an attached SCP affect all IAM users, groups, and roles for an account, including the AWS account root user.


###### Organizations setup
To create and set up an organization, follow these steps:
- Step 1: Create your organization with your current AWS account as the management account. This process assumes that you have administrator permissions in your current account. After you create an organization, you can add accounts to it by creating new accounts or inviting existing accounts to join using the management account.
- Step 2: Create organizational units (OUs) in your new organization and move the member accounts in to those OUs.
- Step 3: Create service control policies (SCPs), which enable you to apply restrictions to what actions can be delegated to users and roles in the member accounts. An SCP is a type of organization control policy.
- Step 4: To test your organization’s policies, sign in as a user for each role in your OUs and see how the service control policies impact account access. Alternatively, you can use the IAM policy simulator to test and troubleshoot IAM and resource-based policies that are attached to IAM users, groups, or roles in your AWS account.

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html

![[Pasted image 20231126105224.png]]

When you create names in AWS Organizations—which includes names of accounts, OUs, roots, and policies—you must follow certain rules. For example, names must be composed of Unicode characters, and can be up to 250 characters in length.
There are a number of other maximum and minimum values for entities in AWS Organizations. Some of the main values are shown in the table.

![[Pasted image 20231126105311.png]]


AWS Organizations is available to all AWS customers at no additional charge. It can be managed through different interfaces:
- The AWS Management Console is a browser-based interface that you can use to manage your organization and your AWS resources. You can perform any task in your organization by using the console.
- The AWS Command Line Interface (AWS CLI) enables you to issue commands to perform AWS Organizations and AWS tasks. The AWS CLI can be faster and more convenient than using the console.
- You can use also AWS software development kits (SDKs) to take care of tasks, such as cryptographically signing requests, managing errors, and retrying requests automatically. AWS SDKs consist of libraries and sample code for various programming languages and platforms, such as Java, Python, Ruby, .NET, iOS, and Android.
- The AWS Organizations HTTPS query API gives you programmatic access to AWS Organizations and AWS. It enables you to issue HTTPS requests directly to the service. When you use the HTTPS API, you must include code to digitally sign requests using your credentials.

Some key takeaways from this lesson include:
- AWS Organizations helps you group AWS accounts so that you can manage them centrally.
- AWS Organizations provides consolidated billing and account management capabilities that help you reach your business goals around budget, security, and compliance.
- The key components in an organization are: 
	- Management account (root) 
	- Organizational unit (OU)
	- Member account 
	- Service control policy (SCP)