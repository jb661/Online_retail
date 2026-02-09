# extract.py
import pandas as pd

def extract_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df

df = extract_data("data/raw/online_data.xlsx")
df.head()
df.info()
