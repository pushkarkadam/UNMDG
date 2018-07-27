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
