import pandas as pd
from io import StringIO


def groupby(csv_string: str) -> str:
    """Problem: Return the country with max count of worker.
    csv_string:
    country|department|num_worker
    US     |DOJ       |60
    JP     |BOJ       |60
    US     |CB        |70
    GB     |CB        |60
    return:
    "US: 130"
    """
    data = StringIO(csv_string)
    df = pd.read_csv(data)
    df = df.groupby("country")["num_worker"].sum().reset_index()
    df = df.nlargest(1, "num_worker")
    return f"{df['country'].values[0]}: {df['num_worker'].values[0]}"
