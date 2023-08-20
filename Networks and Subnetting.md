
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





![[Pasted image 20230820114129.png]]










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


