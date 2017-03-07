import csv
import pandas as pd
from pandas.stats.api import ols
df = pd.read_csv('/home/paddy/py_models/PPNR_Models/USNIM.csv')
df["Slope"] = df['12M'] - df['1M']
results = ols(y=df['NIM'], x= df[['1M', '12M' , 'Slope', 'CPI']])
print(results)

