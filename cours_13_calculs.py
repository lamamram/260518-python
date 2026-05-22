# %% ----- import

import pandas as pd
import numpy as np
from time import time
rng = np.random.default_rng(seed=int(time()))
pd.__version__

# %% ---------- data 

url = "http://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

pg_df = pd.read_csv(
    url,
    encoding="utf8"
)
pg_df
# %% ----------------- aggregates
# aggrégats standards
pg_df.describe()
# un agg sur une colonne
pg_df["bill_length_mm"].median()


# selection auto des colonnes de types données
pg_df.select_dtypes(include=["float64"])

## plusieurs aggs sur plusieurs colonnes
def quartile(s: pd.Series):
  return s.quantile(0.25)

## aggrégat paramétré ==> fermeture en python
# moyenne des n plus lourds
def avg_top(n: int):
  def func(s: pd.Series):
    ## trier sort_values / sclicing sur colonne .iloc[:]
    return s.sort_values(ascending=False).iloc[:n].mean()
  func.__name__ = f"avg_top_{n}"
  return func

pg_df.agg({
  # mean => inclus dans pd, std de np
  "bill_length_mm": ["mean", np.std],
  "body_mass_g": [quartile, avg_top(5)]
})
# %% ----------- vectorisation des séries = colonnes

pg_df["body_mass_g"] /= 1000
# renommer sur les indexes axis=0 / sur les colonnes axis=1
pg_df = pg_df.rename({"body_mass_g": "body_mass_kg"}, axis=1)
pg_df

# %% ----------- vectorisation multi colonne

pg_df["bill_vol_cm3"] = np.around(1/3 * pg_df["bill_depth_mm"] * np.pi * (pg_df["bill_length_mm"]/2)**2 / 1000, 2)
pg_df["bill_vol_cm3"]


# %%
