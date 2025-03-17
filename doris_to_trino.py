from pyspark.sql import SparkSession

# 建立 Spark 會話
spark = SparkSession.builder \
    .appName("DorisToIceberg") \
    .config("spark.sql.catalog.doris", "org.apache.spark.sql.execution.datasources.jdbc.JdbcRelationProvider") \
    .getOrCreate()

# 設定 Doris JDBC 連線
jdbc_url = "jdbc:mysql://HOST:9030/DATABASE_NAME"
properties = {
    "user": "root",
    "password": "",
    "driver": "com.mysql.jdbc.Driver"
}

# 讀取 Doris 資料表
df = spark.read.jdbc(url=jdbc_url, table="TABLE_NAME", properties=properties)
df.show()

# 設定 Trino JDBC 連線
trino_jdbc_url = "jdbc:trino://trino:8080/CATALOG_NAME/SCHEMA_NAME"

# 將 Doris 資料寫入 Iceberg（透過 Trino）
df.write \
    .format("jdbc") \
    .option("driver", "io.trino.jdbc.TrinoDriver") \
    .option("url", trino_jdbc_url) \
    .option("dbtable", "TABLE_NAME") \
    .option("user", "USER") \
    .option("batchsize", "1") \
    .option("isolationLevel", "NONE") \
    .mode("append") \
    .save()
