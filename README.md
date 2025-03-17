# Doris To Trino Data Pipeline Spark

Demonstrating how to use a Spark data pipeline to import Doris data into Iceberg created in Trino.  
It's not an ideal approach, but since Doris cannot set the S3 region (refer to [Github [Bug] S3 properties not work wher create iceberg catalog](https://github.com/apache/doris/issues/23671)), it serves as a temporary solution.