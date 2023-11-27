## Activity overview

In this activity, you will optimize the AWS resources that are used to run the Café web application. Specifically, you will:

1. Uninstall the decommissioned local database from the Café instance to decrease the instance’s storage requirements.
    
2. Change the instance type to T3 micro to reduce costs.
    
    This diagram illustrates the topology of the Café web application runtime environment _before_ and _after_ the optimization.

**Before and after resource optimization topology diagrams:**
![[optimize-resources-architecture.png]]

## Activity objectives
After completing this activity, you will be able to:
- **Optimize** an Amazon Elastic Compute Cloud (Amazon EC2) instance to reduce costs.
- **Use** the AWS Pricing Calculator to estimate AWS service costs.

## Business case relevance

**A new business requirement for Café—Optimize resources to reduce AWS service costs**
After the migration to Amazon Relational Database Service (Amazon RDS) was completed (an action taken in a prior activity), Sofîa identified a number of optimization opportunities that she could implement to reduce AWS service costs. First, she realized that the decommissioned local database could be uninstalled to reduce the storage requirements of the Café instance. She also realized that the Café instance could be downsized to a smaller instance type because the database process was no longer running on it.

In this activity, you will take on the role of Sofia, and work on optimizing the Café instance to save costs.

## Task 1: Optimize the website to reduce costs
Because the local database was migrated to Amazon RDS, you can reduce AWS service costs by performing the following actions on the Café EC2 instance:
- Remove the local database from the instance. This action will reduce costs in both CPU and storage utilization.
- Change the instance type from t3.small to _t3.micro_. Because the database process no longer runs on the instance, the smaller instance type will be both effective and also cheaper to run.

In this task, you use the AWS Command Line Interface (AWS CLI) to perform these actions. You begin by opening a Secure Shell (SSH) session to the _Café instance_ and the _CLI Host_.

In order to optimize our EC2 instance, first we are going to uninstall MariaDB and then resize the instance.

In order to stop the local database and uninstall it from the Café instance, we need to run the following scripts:

```bash
sudo systemctl stop mariadb
```

```bash
sudo yum -y remove mariadb-server
```

Then we disconnect from the Cafe Instance and connect to the CLI-Host instance.

Once connected, we run the following command in order to determine the CafeInstance Instance ID from the CLI-Host EC2 instance:
```bash
aws ec2 describe-instances \

--filters "Name=tag:Name,Values= CafeInstance" \

--query "Reservations[*].Instances[*].InstanceId"
```
And we get the following output:
![[Pasted image 20231127183236.png]]
```bash
[
    [
        "i-0534398156444c857"
    ]
]
```

Now, we need to stop the Café instance and change its instance type from t3.small to t3.micro. In order to achieve that, we run the following command:
```bash
aws ec2 stop-instances --instance-ids i-0534398156444c857
```
And we get the following output:
![[Pasted image 20231127183525.png]]

Next, we run the command that downgrades the instance from a t3.small to a t3.micro instance.
```bash
aws ec2 modify-instance-attribute \

--instance-id i-0534398156444c857 \

--instance-type "{\"Value\": \"t3.micro\"}"
```

Then, we run the following command in order to start the instance back up:
```bash
aws ec2 start-instances --instance-ids i-0534398156444c857
```
