## CI
CI is a practice of integrating code from multiple developers into a central repo or branch, multiple times per day


CI build consists of automated processes that:
run automatic code quality scan and generate report how well latest code changes adhere to good coding practives

build code and run any automated tests that are written to make sure the changes don't break any functionality

generate and publish a test coverage report

CI: Build code and testing the code, saving the image/code
If CI did not go through, we cant deploy the application to the consumers

![[Pasted image 20231206092405.png]]

The testing result is usually sent to the developers to get a grasp on the status of their code/application validity


----
## CD
Continuous Delivery, Continuous Deployment
![[Pasted image 20231206093324.png]]
![[Pasted image 20231206093729.png]]
CD does not eliminate the work of QA, QA is usually done on the application that is already in production. It is possible that QA passes code that checks certain things that QA would like to see tested before the application goes into production, saving them time 



![[Pasted image 20231206094103.png]]![[Pasted image 20231206094114.png]]

![[Pasted image 20231206094740.png]]

