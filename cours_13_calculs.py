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
