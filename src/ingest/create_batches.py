import os
import pandas as pd
from datetime import datetime, timedelta

# Đường dẫn file gốc
INPUT_FILE = "hotel_bookings.csv"

# Thư mục lưu dữ liệu raw sau khi tạo batch
OUTPUT_DIR = "data/raw"

# Số batch muốn tạo
NUM_BATCHES = 7

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Đọc dữ liệu gốc từ Kaggle
df = pd.read_csv(INPUT_FILE)

# Ngày bắt đầu mô phỏng thu thập dữ liệu
start_date = datetime(2026, 5, 1)

for i in range(NUM_BATCHES):
    batch_df = df.copy()

    # Tạo ngày thu thập giả lập
    collection_date = start_date + timedelta(days=i)

    # Thêm 2 cột mới để phân biệt từng batch
    batch_df["collection_date"] = collection_date.strftime("%Y-%m-%d")
    batch_df["batch_id"] = f"batch_{i+1:02d}"

    # Tên file output
    output_file = os.path.join(
        OUTPUT_DIR,
        f"hotel_bookings_batch_{i+1:02d}.csv"
    )

    # Lưu thành CSV
    batch_df.to_csv(output_file, index=False)

    print(f"Created: {output_file}")

print("Batch data creation completed.")