from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum as spark_sum


spark = SparkSession.builder \
    .appName("HotelBookingAnalysis") \
    .getOrCreate()

input_path = "hdfs:///user/maria_dev/hotel_booking/processed"
df = spark.read.parquet(input_path)

# 1. Monthly booking trend
monthly_trend = df.groupBy("arrival_date_month") \
    .agg(count("*").alias("booking_count")) \
    .orderBy("booking_count", ascending=False)

monthly_trend.show(20)

# 2. Cancellation rate by hotel type
cancellation_by_hotel = df.groupBy("hotel") \
    .agg(
        count("*").alias("total_bookings"),
        spark_sum("is_canceled").alias("canceled_bookings"),
        (spark_sum("is_canceled") / count("*")).alias("cancellation_rate")
    )

cancellation_by_hotel.show()

# 3. Top customer countries
top_countries = df.groupBy("country") \
    .agg(count("*").alias("booking_count")) \
    .orderBy(col("booking_count").desc())

top_countries.show(10)

# 4. Average daily rate by hotel type
adr_by_hotel = df.groupBy("hotel") \
    .agg(avg("adr").alias("average_daily_rate"))

adr_by_hotel.show()

spark.stop()