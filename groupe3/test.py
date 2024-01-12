import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('France_Energy_1965_2021.csv',index_col=0)
df_cleaned = df.fillna(method='ffill').fillna(method='bfill')
df_cleaned
