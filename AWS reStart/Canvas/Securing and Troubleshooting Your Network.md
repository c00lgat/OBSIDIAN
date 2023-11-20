![[Pasted image 20231119203514.png]]
1. Route tables are the most broadly scoped level of security. Having a private subnet with no direct path to the internet is one of the best ways to protect our internal computing resources against unauthorized access.

2. Second level is *network access control lists (network ACLs)*. Network ACLs enable us to define the default security behavior for our subnets. The VPC or subnet layer security is typically controlled by the network security team. 

3. At the third level, security groups can be used to control behavior at the level of an instance or elastic network interface.

4. At the fourth level, you might choose to use some form of third-party, host-based detection software that monitors individual Amazon Elastic Compute Cloud (Amazon EC2) instances for specific threats (such as malware intrusion, known operating system bugs, and security auditing).

#### Security groups
- Allows traffic to or from an elastic network interface (NICs)
- Stateful - If rules allow traffic to flow in one direction, responses can automatically flow in the opposite direction.
- Configured by default to:
	- Deny all inbound traffic
	- Allow all outbound traffic

- A VPC has a *default security group* that denies all inbound traffic and allows all outbound traffic.
- When an instance in a VPC is launched without specifying a security group for it, the instance is automatically assigned to the default security group.
- We can specify allow rules but no deny rules.
- All rules are evaluated before its decided whether to allow traffic or not.
- All outbound traffic in response to inbound requests us permitted.
Security groups are usually configured with the help of the application development team because they understand which ports and protocols the application uses.

#### Network access control lists
`Network access control lists (network ACLs):`
- Allow a