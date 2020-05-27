# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:39:37 2020

@author: scaryalberto7
descriione: salviamo un dizionario con pickle
tale libreria serve per salvare gli oggetti in file... e nn solo stringhe ecc
"""

# Save a dictionary into a pickle file.
import pickle

import pandas as pd
import numpy as np





dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))


pickle.dump(df, open("save.p", "wb"))  # save it into a file named save.p


# -------------------------------------------------------------
# Load the dictionary back from the pickle file.

df_new = pickle.load(open("save.p", "rb"))
print(df_new)


