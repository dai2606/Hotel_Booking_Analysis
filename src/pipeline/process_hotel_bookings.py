from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark = SparkSession.builder \
    .appName("HotelBookingPreprocessing") \
    .getOrCreate()

input_path = "hdfs:///user/maria_dev/hotel_booking/raw/*.csv"
output_path = "hdfs:///user/maria_dev/hotel_booking/processed"

df = spark.read.csv(input_path, header=True, inferSchema=True)

# Chọn các cột cần phân tích
selected_df = df.select(
    "hotel",
    "is_canceled",
    "lead_time",
    "arrival_date_year",
    "arrival_date_month",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "country",
    "market_segment",
    "customer_type",
    "adr",
    "reservation_status",
    "reservation_status_date",
    "collection_date",
    "batch_id"
)

# Xử lý dữ liệu thiếu cơ bản
clean_df = selected_df.na.fill({
    "children": 0,
    "country": "Unknown",
    "adr": 0
})

# Lọc dữ liệu bất thường
clean_df = clean_df.filter(col("adr") >= 0)
clean_df = clean_df.filter(col("adults") > 0)

clean_df.write.mode("overwrite").parquet(output_path)

print("Preprocessing completed.")
spark.stop()