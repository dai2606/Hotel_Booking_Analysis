# -*- coding: utf-8 -*-

import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIGURE_DIR = "output/figures"

if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)


def read_csv_file(path):
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


# 1. Monthly booking trend
monthly_data = read_csv_file("output/results/monthly_booking_trend.csv")
months = [row["arrival_date_month"] for row in monthly_data]
booking_counts = [int(row["booking_count"]) for row in monthly_data]

plt.figure(figsize=(10, 6))
plt.bar(months, booking_counts)
plt.xticks(rotation=45)
plt.title("Monthly Booking Trend")
plt.xlabel("Month")
plt.ylabel("Booking Count")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "monthly_booking_trend.png"))
plt.close()


# 2. Cancellation rate by hotel
cancel_data = read_csv_file("output/results/cancellation_rate_by_hotel.csv")
hotels = [row["hotel"] for row in cancel_data]
cancel_rates = [float(row["cancellation_rate"]) for row in cancel_data]

plt.figure(figsize=(8, 5))
plt.bar(hotels, cancel_rates)
plt.title("Cancellation Rate by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Cancellation Rate")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "cancellation_rate_by_hotel.png"))
plt.close()


# 3. Top 10 countries
country_data = read_csv_file("output/results/top_countries.csv")[:10]
countries = [row["country"] for row in country_data]
country_counts = [int(row["booking_count"]) for row in country_data]

plt.figure(figsize=(10, 6))
plt.bar(countries, country_counts)
plt.title("Top 10 Countries by Booking Count")
plt.xlabel("Country")
plt.ylabel("Booking Count")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "top_countries.png"))
plt.close()


# 4. Average daily rate by hotel
adr_data = read_csv_file("output/results/adr_by_hotel.csv")
adr_hotels = [row["hotel"] for row in adr_data]
adr_values = [float(row["average_daily_rate"]) for row in adr_data]

plt.figure(figsize=(8, 5))
plt.bar(adr_hotels, adr_values)
plt.title("Average Daily Rate by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Average Daily Rate")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "adr_by_hotel.png"))
plt.close()

print("Visualization completed.")
