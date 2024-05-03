import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Remove commas and spaces at the end of each cell
df = df.applymap(lambda x: x.rstrip(', ').rstrip(',') if isinstance(x, str) else x)

# Save the modified DataFrame back to a CSV file
df.to_csv('data_modified.csv', index=False)