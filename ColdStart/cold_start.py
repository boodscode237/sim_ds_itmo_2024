import pandas as pd
import numpy as np


def fillna_with_mean(df: pd.DataFrame, target: str, group: str) -> pd.DataFrame:
    df_copy = df.copy()

    group_means = df_copy.groupby(group)[target].transform("mean")

    df_copy[target] = df_copy[target].fillna(np.floor(group_means))

    return df_copy
