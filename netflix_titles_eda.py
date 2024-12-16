from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Netflix EDA") \
    .getOrCreate()

# Load the dataset
file_path = "/data/netflix_titles.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Display the schema
print("Schema of the dataset:")
df.printSchema()

# Count of rows and columns
print(f"\nNumber of rows: {df.count()}, Number of columns: {len(df.columns)}")

# Display the first few rows
print("\nFirst 5 rows:")
df.show(5)

# Check for missing values
print("\nMissing values per column:")
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()

# Count movies vs TV shows
print("\nCount of Movies and TV Shows:")
df.groupBy("type").count().show()

# Top 5 genres
print("\nTop 5 Genres:")
df.groupBy("listed_in").count().orderBy(col("count").desc()).show(5)

# Top 5 countries producing content
print("\nTop 5 countries producing content:")
df.groupBy("country").count().orderBy(col("count").desc()).show(5)

# Content added over years
print("\nContent added by year:")
df.select(col("release_year").alias("Year")) \
    .groupBy("Year").count().orderBy(col("Year").desc()).show(10)

# Stop Spark session
spark.stop()
