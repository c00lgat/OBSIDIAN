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