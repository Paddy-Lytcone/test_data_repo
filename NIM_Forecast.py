import csv 
import pandas as pd
from pandas.stats.api import ols
df = pd.read_csv('/home/paddy/py_models/PPNR_Models/USNIM.csv')
results = ols(y=df['NIM'], x= df[['6M' , '1M', '12M', 'CPI']])
print(results)