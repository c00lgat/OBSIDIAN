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
