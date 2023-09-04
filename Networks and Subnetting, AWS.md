
Resources:
https://book.systemsapproach.org/index.html

https://school.kotar.cet.ac.il/KotarApp/Viewer.aspx?nBookID=97613613#24.8046.6.default

https://gaia.cs.umass.edu/kurose_ross/lectures.php

https://www.youtube.com/playlist?list=PLLFIgriuZPAcCkmSTfcq7oaHcVy3rzEtc

https://drive.google.com/file/d/14q9nN-f1W8TMooRQVgAPH9gAn1AGvMOR/view?usp=sharing

---
## Network devices

- Hosts are any devices which send or receive traffic
	- PC, phones, laptops, servers, printers, cloud servers
	- Any IoT devices
- Anything that sends or receives traffic

Two kinds of hosts: 
- Clients and Servers
Client initiates requests, Servers respond
	Relative to specific communication, meaning that A server can become the client in some instances, such as if a server were to update its files, it has to connect to a File Server and ask for the updated files. In this instance, the server becomes the client.

Servers are simply computers with software installed which responds to specific requests.

---
## IP Addresses 
We can think of it as a phone number, we need a phone number before we make a call to the said phone. 
IP Addresses allow for communication between a client and a server.

SRC = source
DST = destination

Every IP address out there is really just a combination of binary numbers:
![[Pasted image 20230820110055.png]]

### IP Hierarchy 
ACME corporation: 10.x.x.x
3  Branches for example:
- New York - 10.20.x.x
	Sales: 10.20.55.x
	Engineering: 10.20.66.x
	Marketing: 10.20.77.x

- London - 10.30.x.x
	Sales: 10.30.55.x
	Engineering: 10.30.66.x
	etc. 

- Tokyo - 10.40.x.x

---
## Network

Before networks, we had to physically interact with the PC, copy the files to a CD And then extract the data to the desired computer, also physically.

A Network is what transports traffic between Hosts. 

Networks can contain other networks. Also called sub-Networks or Subnets.
- For example:
	A school has many classrooms. And each classroom has its own sub-networks.

How is a Coffee Shop connected to Home WIFI connected to School network? There exists a point which connects them all, usually an ISP(?)

---
## Repeater

Data crossing a wire decays as it travels. 
Signal can decay the bigger and longer the distances. 

A repeater regenerates signals.

### Hubs
Connecting hosts directly does not scale. 
Instead of connecting 5 computers to each other, we could connect them to a single point called a Hub.
![[Pasted image 20230820111120.png]]

A computer could simply send a single signal instead of 3 different signals to 3 different computers, the computer could send the signal to a hub, which in turn it sends the signal to the rest of the computers.

The problem is that a hub sends the signal to all computers. What if we wanted to send the signal to one specific computer?

### Bridges
![[Pasted image 20230820111242.png]]
Bridges can isolate between different hubs.

A bridge can be asked to send certain information to the rest of the hubs if needed.


### Switch
A switch is able to send a signal to a specific computer from one to another. And is not limited like a Hub is. 
Multiple computers connected to the same switch are considered a single network.
![[Pasted image 20230820111509.png]]
Each computer/device has its own IP, with the first 3 slots in the IP representing the entire network and the last slot is reserved for the specific device within the network.

![[Pasted image 20230820111631.png]]
Since the two classrooms have different needs and different kind of connectivity and belong to a different class then it is a good idea to isolate the two networks making them a different network each of its own. 

We can let the two networks communicate using a Router:
![[Pasted image 20230820111738.png]]
If .11 computer were to talk to computer .44, the signal is sent through the router and to the computer .44.

Routers learn which networks they are attached to. It knows which two or more networks it routes between.
A routing table contains all the networks a router should know of.

A router has a different IP in each network.
![[Pasted image 20230820111944.png]]
Default gateway is the IP of the router that connects one network to another.

A router can connect between multiple routers. 
![[Pasted image 20230820112106.png]]

The internet is nothing more than different routers connected together.

Note:
<mark style="background: #FFF3A3A6;">Routing is the process of moving data between networks. 
A Router is a device whose primary purpose is routing</mark>

<mark style="background: #FFF3A3A6;">Switching is the process of moving data within networks. A switch is a device who's primary purpose is Switching.
</mark>

Main takeaways:
![[Pasted image 20230820112329.png]]

---
## OSI Model











---

Subnetting series on YouTube
https://www.youtube.com/watch?v=5WfiTHiU4x8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF

Subnetting knowledge helps in everything IT: Networking, Ethical Hacking, Security, Cloud etc.

What is an IP? 
IP stands for Internet Protocol. 

IP address is kind of a phone number. If a device wants to send another device a message, it is done through IP addresses. Without an IP address, devices cannot talk. 
So, we give them IP addresses. So that anything that is connected to the internet can talk to anything else that is also connected to the internet.


To figure out what our IP is: We can just run `ifconfig` in our terminal (Linux, MAC).

An IP consists of 4 sets of numbers and 3 dots separating each set: `192.168.1.204` for example.
Net Mask = Subnet Mask. Same thing.

How did our device get an IP address in the first place? 
We have a router. In our homes, work etc.
Each time a device connects to our router, the router just gives our devices an IP address! 
![[Pasted image 20230816100643.png]]
This dark and mysterious magic is called DHCP and that's why it works.

How and why our IP addresses always start with `192.168.1`? Well, just because. The reasons behind that are complex and we are not going to be going into it for now.
Mr. Subnet Mask kind of decides that for us. Mr. Subnet Mask looks weird and mysterious, lets take a look:
![[Pasted image 20230816101215.png]]
As we pointed out earlier, Mr. Subnet Mask is also known as netmask. 

`255.255.255.0` does look pretty similar to an IP address.
`192.168.1.204`
`255.255.255.0`
We could see that every set of numbers in an IP address matches up with a set of numbers in the netmask.
![[Pasted image 20230816101626.png]]
Each section that is separated by a dot in IP addresses
When we see a 255


---
Enhanced networking on our instance

hping3 packet assembler and analyzer measures end to end packet loss

![[Pasted image 20230829094526.png]]

`traceroute` shows the path that the connection took in order to arrive to the destination node.
![[Pasted image 20230829094752.png]]

`mtr` provides continual updated output which we can use to analyze network performance
![[Pasted image 20230829094917.png]]

`telnet` to check whether a port is open or not
![[Pasted image 20230829094947.png]]


`nslookup` for querying the DNS to obtain the mapping between domain name and IP address or other DNS records
![[Pasted image 20230829095031.png]]

![[Pasted image 20230829103050.png]]
#### Layer 3 (network): The ping and traceroute commands
`ping -c 5` - the -c options stands for count, meaning, the command requests a total of 5 pings to the host
Usually, ping is used to test connectivity to something such as a server. 
Since the ping command uses the ICMP protocol, it sends ICMP echo requests from our machine to the server that you are trying to reach.
Then, the server sends an echo reply back with a round-trip time. 
Used mostly to troubleshoot connectivity issues and reachability to a specific target.
Can also be used to bring a specific network up if traffic needs to continuously flow through a network. 
We can also send a continuous ping.



Here is a scenario in which a customer is having latency issues. 

> The customer is having latency issues. They say that their connection is taking a long time, and they are having packet loss. They aren't sure if it is related to AWS or their internet service provider (ISP). To investigate, you can run the traceroute command from their AWS resource to the server that they are trying to reach. If the loss happens toward the server, the issue is most likely the ISP. If the loss is toward AWS, you might need to investigate other factors that might limiting networking connectivity.

The `traceroute` command shows the path taken to the webserver and the latency taken to it.
Packet loss can be seen with the `traceroute` command as percentage and can occur at each hop. Usually occurs because of an issue with the user's local area network or ISP.
However, if the packet loss occurs towards the end of the route, then the issue is more than likely the server connection. We can pinpoint an issue or error when hostnames and IP addresses on either side of a failed jump.


If an issue or error occurs, we should see that as three asterisks (\*\*\*) which indicate a failed hop.


#### Layer 4 (transport): The netstat and telnet commands
Here is a following customer scenario in which we could use the `netstat` command:
>Your company is running a routine security scan and found that one of the ports on a certain subnet is compromised. To confirm, you run the netstat command on a local host on that subnet to confirm if the port is listening when it shouldn't be.

```bash
netstat -tp
```

`netstat -tp`: confirms established connections

`netstat -tlp`: outputs listening services
`netstat -ntlp` outputs listening services but does not resolve port numbers

The `netstat` command shows the current established TCP connections from which the host is listening. 
When troubleshooting networking issues starting with the host machine and working outward, we can run this command to understand which ports are listening and which are not.
Because this command gives you a snapshot of your layer 4 connectivity, using this command will help you save time when trying to narrow down a large networking issue.


The following is an example of a customer scenario where you can use the `telnet` command:
>The customer has a secure web server and has custom security group rules and network ACL rules configured. However, they are concerned that port 80 is open even though it shows their security settings indicate that their security group is blocking this port, you can run telnet 192.168.10.5 80 to ensure that the connection is refused.

```bash
telnet www.google.com 80
```

The telnet command confirms the TCP connection to a web server. It makes the HTTP request using telnet.

The telnet command confirms the TCP connection to a web server making an HTTP request if using port 80 to telnet. You can also use this command at layer 7. If you can successfully connect to the web server, then there is nothing blocking you or the server from connecting. If the connection fails with a message like "connection refused," then something is likely blocking the connection, such as a firewall or security group. If the connection fails with a message like "connection timed out," then then issue may be no network route or connectivity.

#### Layer 7 (application): The curl command

The following is an exmaple of a customer scenario where you can use the `curl` command:
>The customer has an Apache server running, and they want to test if they are getting a successful request (200 OK), which indicates that their website is running successfully. You run a curl request to see if the customer's Apache server returns a 200 OK.

```bash
curl -vLo /dev/null https://aws.com
```

This is the `curl` command. You can use the following command options:

-I: This option provides header information and specifies that the request method is Head.

-i: This option specifies that the request method is GET.

-k: This option tells the command to ignore SSL errors.

-v: This option is verbose. It shows what the computer is doing or what the software is loading during startup.

-o /dev/null: This option will send HTML and CSS in response to null.

_The results of the curl command: the output tests the connection to a web service, such as AWS, and submits the HTTP request._

We can use the `curl` command to transfer data between you and the server. the `curl` command can use many different protocols but the most common are HTTP and HTTPS. We can use the `curl` command to troubleshoot communication from your local device to a server.

---
## Troubleshooting a Network Issue
Lab 266 - amazon canvas

Email from Customer:
> Hello, Cloud Support!
> 
> When I create an Apache server through the command line, I cannot ping it. I also get an error when I enter the IP address in the browser. Can you please help figure out what is blocking my connection?
> 
> Thanks!
> 
> Ana Contractor

![[aym6iug9.bmp]]
_Figure: The customer's virtual private cloud (VPC) architecture._

In the scenario, Ana, the customer requesting assistance, cannot reach her Apache server or get it to successfully load on a webpage from her virtual private cloud (VPC).

```bash
sudo systemctl status httpd.service
```
![[qc5uecqg.bmp]]
_Figure: The status shows that the httpd service is inactive because it has not been started yet. This output indicates that the httpd service is loaded (already installed) but is currently inactive._

```bash
sudo systemctl start httpd.service
```
```bash
sudo systemctl status httpd.service
```
![[obatqql3.bmp]]
_Figure: The Apache HTTP Server should be in the Active status._
The httpd service is now running. 

Once we made sure the httpd is up and running, we have to make sure that:
- Subnets - Are the route tables associated to the correct subnets?
- Route Tables - Do the route tables have the correct routes?
- Internet Gateway - Is there an Internet Gateway and is it attached?
- Security Groups and network ACLs - Are the correct rules configured?
In this specific lab, the security group was not allowing any HTTP traffic in the inbound table, meaning port 80 was not whitelisted.
Once we allow HTTP traffic, we are then able to connect to our EC2 through the browser by entering the EC2 IP into the URL textbox in the browser.

---
## Build Your VPC and Launch a Web Server - Lab 267

In this lab, you use Amazon Virtual Private Cloud (VPC) to create your own VPC and add additional components to produce a customized network for a Fortune 100 customer. You also create security groups for your EC2 instance. You then configure and customize an EC2 instance to run a web server and launch it into the VPC that looks like the following customer diagram:
![[qb48ajdh.bmp]]
_Figure: The customer is requesting the build of this architecture to launch their web server successfully._

We use the VPC wizard to start a VPC. 
An internet gateway and two subnets. An internet gateway is a CPV component that allows communication between instances in your VPC and internet.

After creating a VPC, we can add subnets. Each subnet resides entirely within one Availability Zone and cannot span zones. 

A subnet is a public subnet if it has an internet 
gateway that routes traffic to the internet.
Otherwise, its a private subnet.

We are also going to be creating a NAT. The NAT is used to connect an EC2 that resides inside a private subnet to the internet.


We set up route tables for the private subnets to route internet-bound traffic to the NAT gateway so that resources in the private subnet are able to connect to the internet while still keeping the resources private.

A route table contains a set of rules, called routes, that are used to determine where network traffic is directed. Each subnet in a VPC must be associated with a route table; the route table controls routing for the subnet.

**Destination 0.0.0.0/0** is set to **Target nat-xxxxxxxx**. This means that traffic destined for the internet (0.0.0.0/0) will be sent to the NAT gateway. The NAT gateway will then forward the traffic to the internet.

---
## Network Hardening
**Amazon Inspector** runs scans that analyze all your network configurations—such as security groups, network access control lists (network ACLs), route tables, and internet gateways—together to infer reachability. You don't need to send packets across the virtual private cloud (VPC) network or connect to Amazon Elastic Compute Cloud (Amazon EC2) instance network ports. It’s like packetless network mapping and reconnaissance.

From Amazon Inspector, you will use the **network reachability package** to analyze your network configurations to find security vulnerabilities in your EC2 instances. The findings that Amazon Inspector generates also provide guidance about restricting access that is not secure.

---

**IAM**

IAM can be used for the following:

- **Manage IAM users and their access:** You can create users and assign them individual security credentials (access keys, passwords, and multi-factor authentication devices). You can manage permissions to control which operations a user can perform.
- **Manage IAM roles and their permissions:** An IAM role is similar to a user in that a role is an AWS identity with permission policies that determine what the identity can and cannot do in Amazon Web Services (AWS). However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it.
- **Manage federated users and their permissions:** You can activate identity federation to allow existing users in your enterprise to access the AWS Management Console, to call AWS application programming interfaces (APIs), and to access resources without the need to create an IAM user for each identity.

>A user group consists of several users who need access to the same data. Privileges can be distributed to the entire group of users rather than to each individual. This option is much more efficient when applying permissions and provides greater overall control of access to resources than applying permissions to individuals.

Managed policies are pre-built policies (built either by AWS or by your administrators) that can be attached to IAM users and user groups. When the policy is updated, the changes to the policy are immediately applied to all users and user groups that are attached to the policy.

- **Effect** indicates whether to **Allow** or **Deny** the permissions.
- **Action** specifies the API calls that can be made against an AWS service (for example, _cloudwatch:ListMetrics_).
- **Resource** defines the scope of entities covered by the policy rule (for example, a specific Amazon Simple Storage Service [Amazon S3] bucket, EC2 instance, or * which means _any resource_).

Instead of a managed policy, it has a **Customer inline** policy, which is a policy assigned to only one user or group. Inline policies are typically used to apply permissions for one-off situations.
Inline policies are typically used to apply permissions for one-off situations.