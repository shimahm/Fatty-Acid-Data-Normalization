import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('normalized_to_be.xlsx')

# Define the columns to be normalized
columns_to_normalize = ['14_0', '16_0', '16_1', '16_2', '18_0', '16_3', '18_1', '20_0', '18_2', '18_3', '20_1', '22_0', '22_1', '24_0']

# Normalize each column by dividing by 'sum' and then multiplying by 100
for col in columns_to_normalize:
    df[col] = (df[col] / df['sum']) * 100

# Optionally, you might want to save this normalized dataset to a new file
df.to_excel('normalized_dataset.xlsx', index=False)
