# etl_pipeline.py
from extract import extract_data
from transform import clean_data, add_features, customer_aggregates
from load import load_data

def run_pipeline():
    df = extract_data("data/raw/online_data.xlsx")
    df = clean_data(df)
    df = add_features(df)
    customer_df = customer_aggregates(df)
    load_data(customer_df, "data/processed/customer_features.parquet")

if __name__ == "__main__":
    run_pipeline()
