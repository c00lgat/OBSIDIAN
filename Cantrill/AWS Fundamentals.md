# \[ASSOCIATESHARED] AWS Public vs Private Services
https://learn.cantrill.io/courses/1820301/lectures/41301617

When talking about private and public services in AWS, it is referred to networking only.

A public service is something that is accessed with a public endpoint. Such as an S3. S3 can be accessed from anywhere.

A private AWS service on the other hand, is a service that runs within a VPC and only things that are within that VPC or things that are connected to that VPC can access the service.

Even though S3 is a public service,