# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum as spark_sum

spark = SparkSession.builder \
    .appName("SaveHotelBookingAnalysisResults") \
    .getOrCreate()

input_path = "hdfs:///user/maria_dev/hotel_booking/processed"
output_base = "hdfs:///user/maria_dev/hotel_booking/output"

df = spark.read.parquet(input_path)

monthly_trend = df.groupBy("arrival_date_month") \
    .agg(count("*").alias("booking_count")) \
    .orderBy(col("booking_count").desc())

cancellation_by_hotel = df.groupBy("hotel") \
    .agg(
        count("*").alias("total_bookings"),
        spark_sum("is_canceled").alias("canceled_bookings"),
        (spark_sum("is_canceled") / count("*")).alias("cancellation_rate")
    )

top_countries = df.groupBy("country") \
    .agg(count("*").alias("booking_count")) \
    .orderBy(col("booking_count").desc())

adr_by_hotel = df.groupBy("hotel") \
    .agg(avg("adr").alias("average_daily_rate"))

monthly_trend.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_base + "/monthly_booking_trend")
cancellation_by_hotel.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_base + "/cancellation_rate_by_hotel")
top_countries.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_base + "/top_countries")
adr_by_hotel.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_base + "/adr_by_hotel")

print("Analysis results saved to HDFS.")
spark.stop()
