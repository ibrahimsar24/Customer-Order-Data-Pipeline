# from extract import extract_json
# from transform import flatten_orders
# from load import load_to_parquet, load_to_csv


# def main():
#     data = extract_json(r"C:\Users\ibrah\OneDrive\Desktop\customer-order-data-pipeline\data")
#     df = flatten_orders(data)
#     load_to_parquet(df, r"C:\Users\ibrah\OneDrive\Desktop\customer-order-data-pipeline\output\processed_orders.parquet")
#     load_to_csv(df, r"C:\Users\ibrah\OneDrive\Desktop\customer-order-data-pipeline\output\processed_orders.csv")

# if __name__ == "__main__":
#     main()

from extract import extract_json
from transform import flatten_orders
from load import load_to_parquet, load_to_csv
import os

def main():
    data_dir = os.path.join("data")
    out_parquet = os.path.join("output", "processed_orders.parquet")
    out_csv = os.path.join("output", "processed_orders.csv")

    data = extract_json(data_dir)
    df = flatten_orders(data)
    load_to_parquet(df, out_parquet)
    load_to_csv(df, out_csv)

if __name__ == "__main__":
    main()
