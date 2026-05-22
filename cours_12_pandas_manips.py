# %%
import pandas as pd
import numpy as np
from time import time
rng = np.random.default_rng(seed=int(time()))
pd.__version__


# %%  -- créer le dataframe à partir du fichier users.csv

user_df = pd.read_csv(
  "./users.csv",
  sep=';',
  encoding='utf-8',
  index_col=0,
  # valeurs arbitraires signifiant une indertiminée => valeur NaN => Not an Number => données manquantes
  na_values=["???", "N/A"]
).astype({
  # i1: entier avec un seul octet
  "age": "i1",
  "size": "f2"
})
print(user_df.dtypes)
user_df

# %% ----------------- manipulation immutable vs mutable ----------

l = [1, 2, 3]
# passage par référence: avec les types mutables (list, dict, ..., DataFrame, ndarray)
# => les deux variables ont la même place en mémoire
#clone = l
clone = l.copy()
clone.append(4)
print(l)

# %%  ----------------- dataframe: immutable vs mutable ---

# immutable
user_df.drop(columns="age")
user_df

# version mutable
user_df.drop(columns="age", inplace=True)
user_df
# %% --------------- accès aux colones et lignes -------------

# une colonne est une Série
print(user_df["age"], type(user_df["age"]))

# sous dataframe avec selection de colonnes
user_df[ ["age", "size"] ]
# %%
