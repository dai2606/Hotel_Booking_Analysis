# -*- coding: utf-8 -*-

import csv
import os
from datetime import datetime, timedelta

INPUT_FILE = "hotel_bookings.csv"
OUTPUT_DIR = "data/raw"
NUM_BATCHES = 7

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

start_date = datetime(2026, 5, 1)

for i in range(NUM_BATCHES):
    collection_date = start_date + timedelta(days=i)
    batch_id = "batch_%02d" % (i + 1)

    output_file = os.path.join(
        OUTPUT_DIR,
        "hotel_bookings_batch_%02d.csv" % (i + 1)
    )

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)

        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)

            header = next(reader)
            header.append("collection_date")
            header.append("batch_id")
            writer.writerow(header)

            for row in reader:
                row.append(collection_date.strftime("%Y-%m-%d"))
                row.append(batch_id)
                writer.writerow(row)

    print("Created: %s" % output_file)

print("Batch data creation completed.")
