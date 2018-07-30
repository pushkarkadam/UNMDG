import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('TrainingSet.csv')


# Filtering the data with the series_code column
booleans = []
series_code_column = data.columns.get_loc("Series Code")

for i in range(data.shape[0]):
    try:
        series_code = float(data.iloc[i,series_code_column])
        if (isinstance(series_code, float)):
            booleans.append(True)
    except ValueError:
        booleans.append(False)
        continue
    print(".",end="")
    
print("Done!")
    
is_long = pd.Series(booleans)

new_data = data[is_long]


X = new_data.iloc[:,:37].values

print(X)
print("----------------------\n-----------------------\n")


# Finding the missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:,1:37])
X[:,1:37] = imputer.transform(X[:,1:37])

print(X)