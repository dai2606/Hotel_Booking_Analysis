#!/bin/bash

echo "Creating HDFS directory..."
hadoop fs -mkdir -p /user/maria_dev/hotel_booking/raw

echo "Uploading raw CSV files to HDFS..."
hadoop fs -put -f data/raw/*.csv /user/maria_dev/hotel_booking/raw/

echo "Checking uploaded files..."
hadoop fs -ls /user/maria_dev/hotel_booking/raw