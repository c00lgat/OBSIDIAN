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
- Does the resource type have all required 