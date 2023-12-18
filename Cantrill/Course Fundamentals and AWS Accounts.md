Think of AWS Accounts as containers for <mark style="background: #FF5582A6;">identities</mark> (users) and <mark style="background: #BBFABBA6;">Resources</mark>.
Only things within the account can access anything else within that same account.

Any IAM identity starts off with no permission. We have to explicitly give the IAM entities permissions to use services.

Cross-account activity is not abled by default.

Creating multiple AWS Accounts; such as a development account, a testing account and a production account, then we can limit the damage in case of system admins doing mistakes, any bad actors intentionally trying to cause damage etc. since AWS Accounts are good at containing the damage done and does not allow the rest of the accounts to be exploited as long as the credentials aren't compromised.

AWS Accounts can also be created for the different teams in the company, or even the different products that each account hosts.

![[Pasted image 20231218123824.png]]

We are going to avoid using the root user because we cannot restrict it. Best practice is creating IAM identities within that root user account. 
We can create an identity called IAMADMIN. Normal IAM user which we are going to give administrative permissions over the general AWS account.

Once we are done creating the General account, we are going to be making a new root user account called Production.
![[Pasted image 20231218130259.png]]

---
![[Pasted image 20231218150106.png]]
Going to the account user in the top right corner, and then clicking on `Security credentials` should take us to the <mark style="background: #FF5582A6;">Identity and Access Management (IAM)</mark> page, specifically the page that has to do with the account's security credentials page.

Then, click on the `Assign MFA device` button after scrolling down a little:
![[Pasted image 20231218150417.png]]
Following through with the setup, we should eventually receive a success message in the AWS Console:
![[Pasted image 20231218150624.png]]

