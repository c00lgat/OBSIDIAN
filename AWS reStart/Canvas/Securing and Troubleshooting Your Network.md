![[Pasted image 20231119203514.png]]
1. Route tables are the most broadly scoped level of security. Having a private subnet with no direct path to the internet is one of the best ways to protect our internal computing resources against unauthorized access.

2. Second level is *network access control lists (network ACLs)*. Network ACLs enable us to define the default security behavior for our subnets. The VPC or subnet layer security is typically controlled by the network security team. 

3. At the third level, security groups can be used to control behavior at the level of an instance or elastic network interface.

4. At the fourth level, you might choose to use some form of third-party, host-based detection software that monitors individual Amazon Elastic Compute Cloud (Amazon EC2) instances for specific threats (such as malware intrusion, known operating system bugs, and security auditing).

#### Security groups
