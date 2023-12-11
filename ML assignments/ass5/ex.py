import pandas as pd
import numpy as np
data = {'A': [1, np.nan, 3, np.nan, 5],
        'B': [10, np.nan, np.nan, 40, 50]}
df = pd.DataFrame(data)

# Forward fill (pad)
df_filled_pad = df.fillna(method='pad')

# Backward fill (bfill)
df_filled_bfill = df.fillna(method='bfill')

print("Original DataFrame:")
print(df)

print("\nDataFrame after Forward Fill (pad):")
print(df_filled_pad)

print("\nDataFrame after Backward Fill (bfill):")
print(df_filled_bfill)
