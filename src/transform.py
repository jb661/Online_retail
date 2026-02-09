# transform.py
import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop rows w/o customer ID
    df = df.dropna(subset=["CustomerID"])

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove cancelled transactions
    df = df[df["Quantity"] > 0]

    # Remove zero or negative prices
    df = df[df["UnitPrice"] > 0]

    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Total transaction value
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Extract time features
    df["InvoiceYear"] = df["InvoiceDate"].dt.year
    df["InvoiceMonth"] = df["InvoiceDate"].dt.month

    # High-value transaction flag
    df["HighValueTxn"] = np.where(
        df["TotalPrice"] > df["TotalPrice"].median(), 1, 0
    )

    return df

def customer_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    customer_df = (
        df.groupby("CustomerID")
        .agg(
            total_spend=("TotalPrice", "sum"),
            total_transactions=("InvoiceNo", "nunique"),
            avg_order_value=("TotalPrice", "mean"),
            first_purchase=("InvoiceDate", "min"),
            last_purchase=("InvoiceDate", "max"),
        )
        .reset_index()
    )

    # Customer lifetime (days)
    customer_df["customer_lifetime_days"] = (
        customer_df["last_purchase"] - customer_df["first_purchase"]
    ).dt.days

    return customer_df
