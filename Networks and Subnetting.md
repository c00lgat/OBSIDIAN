
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

ACME corporation: 10.x.x.x
New York - 10.20.x.x
	Sales: 10.20.55.x
	Engineering: 10.20.
London - 10.30.x.x
Tokyo - 10.40.x.x




















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


