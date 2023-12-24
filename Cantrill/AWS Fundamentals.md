# \[ASSOCIATESHARED] AWS Public vs Private Services
https://learn.cantrill.io/courses/1820301/lectures/41301617

When talking about private and public services in AWS, it is referred to networking only.

A public service is something that is accessed with a public endpoint. Such as an S3. S3 can be accessed from anywhere.

A private AWS service on the other hand, is a service that runs within a VPC and only things that are within that VPC or things that are connected to that VPC can access the service.

Even though S3 is a public service, by default, an identity other than the account root user has no authorization to access that resource.

Two zones:
- Public internet zone
	- Online games
	- Gmail
	- Online stores

- "AWS Private" Zone
	- VPCs
	- EC2 Instances inside VPCs
Nothing from the internet can access these services unless you configure it.

There is actually a third zone:
"AWS PUBLIC" Zone.
This runs between the Public Internet and the AWS Private Zone networks.
It is not on the public internet and is not part of the public internet but rather is connected to the public internet.

It is the zone where services with public endpoints, such as S3, run.

Private networks can be connected together but only if we decided to allow and configure it that way.
On-Premises for example can access VPCs only if configured via VPN or physically using Direct Connect.

An IGW (Internet Gateway) can be attached to a VPC which will give the VPC added functionality, it will let private zone resources to access the internet, as long as the resource in the VPC, such as an EC2, is allocated a public IP address.
It also allows access to Public AWS services such as S3 but it is important to keep in mind that the data does not touch the public internet at any point during this connection.

---
# \[ASSOCIATESHARED] AWS Global Infrastructure
https://learn.cantrill.io/courses/1820301/lectures/41301618


