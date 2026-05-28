#!/bin/bash

hadoop fs -mkdir -p /user/maria_dev/hotel_booking/raw

hadoop fs -put -f data/raw/*.csv /user/maria_dev/hotel_booking/raw/

hadoop fs -ls /user/maria_dev/hotel_booking/raw