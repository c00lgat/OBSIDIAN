Think of AWS Accounts as containers for <mark style="background: #FF5582A6;">identities</mark> (users) and <mark style="background: #BBFABBA6;">Resources</mark>.
Only things within the account can access anything else within that same account.

Any IAM identity starts off with no permission. We have to explicitly give the IAM entities permissions to use services.

Cross-account activity is not abled by default.

Creating multiple AWS Accounts; such as a development account, a testing account and a production account, then we can limit the damage in case of system admins doing mistakes, any bad actors intentionally trying to cause damage etc. since AWS Accounts are good at containing the damage done and does not allow the rest of the accounts to be exploited as long as the credentials aren't hacked.

AWS Accounts can also be created for the different teams in the company, or even the different products that each account hosts.

![[Pasted image 20231218123824.png]]

