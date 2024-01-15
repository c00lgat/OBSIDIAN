### Evolution of Cloud + Infrastructure as Code
- Infrastructure provisioned via APIs
- Servers created and destroyed in seconds
- Long-lived + mutable -> Short-lived + immutable
	- Rather than having a server that is up for years on end and is being modified, different dependencies are being installed and changed and patched. 
	- Nowadays, when a server needs to be modified, we can just spin up a brand new server with those dependencies already installed.
	- So every server in the cloud now is usually short-lived immutable thing that we are never gonna change. 
	- Paradigm shift.

### Provisioning Cloud Resources:
# GUI
![[Pasted image 20240115123359.png]]

# API/CLI
![[Pasted image 20240115123414.png]]
# IaC
![[Pasted image 20240115123434.png]]IaC enables you to take your entire infrastructure and define it in the code base. 
It lets us know what is exactly positioned at any given time.
Provisioning multiple environment makes it harder to do so using the GUI, so defining things as code as configurations within the code base, we have much higher confidence telling what we have actually deployed, and use the power of programming languages to have multi
