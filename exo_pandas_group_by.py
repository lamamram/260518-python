# %% [markdown]
# ### TITANIC
# * à partir de l'url suivante: 
#   [http://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv](http://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)
# 
# * scruter les données, les **champs utiles** ...
# * calculer le **nb, la somme et le pourcentage de survivants** chez **les femmes et les enfants** par **classe**
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time
rng = np.random.default_rng(seed=int(time()))
pd.__version__

URL = "http://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

def percent(s: pd.Series):
    return np.around(s.sum()/s.count() * 100, 1)

# %%
titanic_df = pd.read_csv(
    URL,
    encoding="utf8"
)
titanic_df.head(20)
# titanic_df.tail(20)

# %%
# 1. élaguer
sub_df = titanic_df.loc[ 
    titanic_df["who"] != "man" , 
    ["survived", "pclass", "who"] 
]
sub_df
# %%
gb = sub_df.groupby(["pclass", "who"])
results = gb["survived"].agg(["count", "sum", percent])

results

# %%
# première utilisation de matplotlib avec un df bien formé et un graphe

results.plot(
    y="percent", 
    kind="pie", 
    figsize=(5, 5), 
    fontsize=5
)
# %%
