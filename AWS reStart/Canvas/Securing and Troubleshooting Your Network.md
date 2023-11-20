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
Network access control lists (network ACLs) are associated with a subnet within a VPC.

`Network access control lists (network ACLs):`
- Allow or deny traffic in and out of subnets
- Default network ACL:
	- Allow all inbound and outbound traffic.
- Stateless:
	- Even if rules allow traffic to flow in one direction, you must explicitly allow responses to flow in the opposite direction.
- Hardens security as a secondary level of defense at the subnet level.
![[Pasted image 20231120071639.png]]
The special rule number \* is evaluated last. It represents a catchall if no match with a prior rule was found.

Once the network ACL is defined, it can be associated to one or more subnets within a VPC.

ACLs are usually administered by the network security or the network administration team.


#### Bastion host
- Provides public-subnet-to-private-subnet access.
	- Jump point to gain access to a private subnet
- Do not store private keys on the bastion host
	- For Linux instances, use the agent forwarding feature of the SSH client to specify the key
	- For Microsoft Windows instances, decrypt the password with the key in the Amazon EC2 console and then add the instance to a domain
Serves as a jump point from the public internet to the EC2 instances and other resources in a private subnet. 

> It is recommended that you use a different set of public-private key pairs for the bastion host and for the resources in the private subnet.
![[Pasted image 20231120092722.png]]


##### Linux bastion host security groups
![[Pasted image 20231120093024.png]]
`Configuring security groups to allow the bastion host to access an instance in your private subnet:`
1. Configure the bastion host to allow only connections from within your corporate network in order to prevent anyone outside the organization from accessing the bastion host.
   > In the example above, only connections from `17.5.0.0/16` address range are accepted by the bastion host. 
   
2. Create a rule in the private instance's security group to allow only incoming connections from the bastion host. In the rule, we can simply add the bastion host's security group, which should contain all the instances that are allowed to connect to the bastion host and in turn, to the private subnet as well.
   
##### Remote desktop gateway as Windows bastion host
![[Pasted image 20231120094725.png]]
If you run Microsoft Windows instances in Amazon EC2, you will probably use RDP for remote administration. To define the source IP addresses that are allowed to connect to the RDP port of your EC2 instance (TCP port 3389), you configure the instance’s security group rules. When you configure your security groups, it is a best practice to apply the principle of least privilege. In this case, least privilege means that you allow only connections to the RDP port from the IP addresses that your administrators will be connecting from, and denying all others. However, in cases where an administrator could connect from anywhere on the internet, it could be difficult to determine which IP addresses to allow. As a result, we often see customers setting security groups for RDP access that allow every IP address (0.0.0.0/0), which fails to enforce least privilege at the network layer.

One solution to this problem is to protect your Microsoft Windows instances at the network layer by using the Microsoft Remote Desktop (RD) Gateway server set up as a bastion host. RD Gateway can be configured to accept connections through HTTPS (TCP port 443) from every IP address on the internet. It then proxies these connections to your other Microsoft Windows instances through RDP port (TCP port 3389). Only users who authenticate to your RD Gateway instance are allowed to proceed to the protected Microsoft Windows instances behind the proxy.

> For more information on configuring a Microsoft Windows bastion host to use RD Gateway, refer to Controlling Network Access to EC2 Instances Using a Bastion Server https://aws.amazon.com/blogs/security/controlling-network-access-to-ec2-instances-using-a-bastion-server/

----
### Common troubleshooting tasks

###### Troubleshooting instance connections
![[Pasted image 20231120144456.png]]

One of the more common issues for Amazon EC2 users is that they cannot connect to an EC2 instance. The slide shows the most common sources of this issue. As an operations professional, you will want to verify that these resources are configured correctly.

First, verify that the instance is running. Also, verify that the security group allows connections over the port or ports that you are attempting to connect to. For example, for SSH connections, verify that port 22 is open. For web server connections, verify that port 80 or port 443 (or both) are open.

Another configuration to verify is whether the public IP address has changed. If you stop an instance and then later start it, it will receive a new public IP address (unless an Elastic IP address is attached to it). Also, verify that the internet gateway and route table settings are correct.

###### Troubleshooting SSH connections

