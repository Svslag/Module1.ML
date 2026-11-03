"""Download the Adult Census dataset from UCI and save it as adult.csv."""
from pathlib import Path
import pandas as pd

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education.num",
    "marital.status", "occupation", "relationship", "race", "sex",
    "capital.gain", "capital.loss", "hours.per.week", "native.country", "income",
]

df = pd.read_csv(URL, header=None, names=COLUMNS, na_values="?", skipinitialspace=True)
df.to_csv(Path(__file__).with_name("adult.csv"), index=False)
print(f"Saved {len(df):,} rows to adult.csv")
