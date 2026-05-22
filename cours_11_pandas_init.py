# %%
import pandas as pd
import numpy as np
from time import time
rng = np.random.default_rng(seed=int(time()))
pd.__version__


# %%
# #### instanciation d'un Dataframe Pandas
data = [
    ["jimmy", 28, "2 rue de la rép, 44000 NANTES", 1.73],
    ["Joan", 33, "12 bd Haussmann 75009 Paris", 1.56],
    ["Paul", 76, "10, chemin des lilas, 13002 MARSEILLE", 1.85],
]

columns = ["name", "age", "address", "size"]
index = ["user1", "user2", "user3"]

# %% -------------- création classique: data | columns | indexes -------------------
df = pd.DataFrame(
  data=data, 
  columns=columns,
  index=index
  # on ajuste tout de suite les types de données attendus
).astype(
  dtype={
    "age": "int8",
    "size": "float16"
})
# dimension 2, (3 lignes x 4 cols) et 12 cellules
df.ndim, df.shape, df.size
# types des colonnes : int64 / float64 ...
df.dtypes
# résumé
# df.info()
# %% --------------- idem avec des colum_set --------------------------------

# données transposées en colonnes
col_data = np.array(data).T.tolist()
# zip les noms de  colonnes et des données
col_set = dict(zip(columns, col_data))
# dictionnaire {clé: données colonne, ...}
print("col_set")
print(col_set)

df = pd.DataFrame(
  data=col_set, index=index
).astype(
  dtype={
    "age": "int8",
    "size": "float16"
})
df

# %% ---------------- idem avec des records (objets JSON) ----------------
# records => objets json => dict
records = np.apply_along_axis(
    lambda row: dict(zip(columns, row)),
    arr=data,
    axis=1
)
print(records.tolist())

df = pd.DataFrame.from_records(
  records,
  index=index
).astype(
  dtype={
    "age": "int8",
    "size": "float16"
})
df
# %% ------------------ écrire en csv -----------------------
df.to_csv(
  # "./users.csv"
  "./users.zip", 
  sep=";",
  encoding="utf-8",
  # pour windows / excel remplacer utf-8 par iso-8859-1
  # préselection de colonnes
  # columns=columns[:-1],
  # ajout ou non de l'index en tant que colonne
  index=False,
  header=True
)

# %% --------------------- lire en csv ----------------------
df = pd.read_csv(
  "./users.zip",
  sep=";",
  encoding="utf-8",
  usecols=columns[:-1],
  # par défaut pandas choppe les colonnes sur la première ligne
  # header=0
)
df

# %% ------------------------- convertir en json ------------------
df.to_json(
  "users.json",
  orient="records",
  force_ascii=False,
  indent=2
)





# %%
