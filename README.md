# Doris To Trino Data Pipeline Spark

Data pipeline written by Spark to transfer Doris to Trino.  
It is not recommended to use a data pipeline for data migration. Instead, you can directly set up an external catalog in Doris to connect to Iceberg. This is just an exceptional example.

## Overview

- Language: Python
- Data Processing Framework: Spark v3.5.1


## Run

```
docker compose up -d
```

