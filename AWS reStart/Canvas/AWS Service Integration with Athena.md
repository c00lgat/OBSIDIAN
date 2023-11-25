Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon Simple Storage Service (Amazon S3) by using standard structured query language (SQL).

Amazon Athena characteristics:
- Handles large scale datasets with ease
- Serverless - avoids need to extract, transform, and load (ETL)
- Pay only for the queries that you run
- Athena automatically runs queries in parallel so most results come back in seconds.

To use Athena, first we have to point it to our data that is sitting in an S3 bucket, define the schema and start querying by using standard SQL.
No need for complex ETL jobs to prepare the data for analysis. 
Makes it easy for anyone with SQL skills to quickly analyze large scale datasets.

Works with various standard data formats, including CSV, JSON, ORC, Apache Avro and Apache Parquet. 
It is ideal for quick, ad hoc querying. It can also handle complex analysis including large joins and arrays.
Amazon S3 acts as the underlying data store for Athena, which makes our data highly available and durable.

Athena is serverless. Meaning no infrastructure to manage, and only pay for the queries that we run.

Athena offers fast, interactive query performance. It automatically runs queries in parallel so that most results come back within seconds.


![[Pasted image 20231125150406.png]]

