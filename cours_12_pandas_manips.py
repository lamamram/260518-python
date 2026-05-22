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
# %% --------------- accès aux colones et lignes avec [] -------------

# une colonne est une Série
print(user_df["age"], type(user_df["age"]))

# sous dataframe avec selection de colonnes
user_df[ ["age", "size"] ]

# %% ------------------ idem avec le slicing [:] ----------

# par défaut [:] => selectionne les lignes
# pas très pratique
user_df[0:-1]

# idem avec les indexes => bonne selection des lignes
user_df.loc["jimmy":"Joan"]

# %% ----------------- selection lignes ET colonnes --------------

# slice ligne sur une colonne => sous - série
user_df.loc["jimmy":"Joan" , "age"]

# sous df slice ligne et selection discrètes de colonnes
user_df.loc["jimmy":"Joan" , ["size","age"] ]

# sous df double slice
user_df.loc[ "jimmy":"Joan" , "age":"size" ]

# %% ----------- filtrage par valeur ---------------

# lignes ayant la colonne "age" inférieure à 40
user_df.loc[ 
  user_df["age"] < 40 , 
  ["size","age"]
]

## plusieurs filtres: & => and, | => or, ~ => not

user_df.loc[ 
  (user_df["age"] < 40) & (user_df["size"] > 1.70) , 
  ["size","age"]
]

# %%
