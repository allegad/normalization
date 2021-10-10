import os
import pandas as pd
from os import path
DATA_DIR = '/Users/david/OneDrive/Documents/Python Projects/data/'
#C:\Users\david\Downloads\ltcwff-files-0.9.0\data
pnl = pd.read_csv(path.join(DATA_DIR, 'leg-pnl.csv'))
#load the position leg pnl data
#what we are doing here is importing libraries (os, pandas), setting DATA_DIR, and loading the player game data into a DataFrame named pg

#normalization and value_counts
#value_counts summarizes the frequency of individual values
print(pnl["Pool"].value_counts())
#we can normalize these frequencies - dividing each by the toal so that they add up to 1 and represent proportions - by passing the normalize=True argument
print(pnl["Pool"].value_counts(normalize=True))

pnl.to_csv(path.join(DATA_DIR, "leg-pnl.pool.csv"))