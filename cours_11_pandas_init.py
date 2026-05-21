# %%
import pandas as pd
import numpy as np
from time import time
rng = np.random.default_rng(seed=int(time()))
pd.__version__


# %%
# #### instanciation d'un Dataframe Pandas

# %%
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
df.info()
# %% --------------- idem avec des colum_set --------------------------------

# données transposées en colonnes

# dictionnaire {clé: données colonne, ...}



# %% ---------------- idem avec des records (objets JSON) ----------------
# records => objets json => dict

# %% ------------------ écrire en csv -----------------------


# %% --------------------- lire en csv ----------------------


# %% ------------------------- convertir en json ------------------






