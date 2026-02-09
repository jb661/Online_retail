# load.py
def load_data(df: pd.DataFrame, path: str):
    df.to_parquet(path, index=False)

