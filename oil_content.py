import pandas as pd

# Step 1: Read your dataset from XLSX file
df = pd.read_excel('normalized_dataset.xlsx')

# Step 2: Perform the calculation
df['oil_content'] = (df['sum'] / df['seed_weight']) * 20

# Step 3: Save the updated dataset to XLSX file
df.to_excel('transformed_dataset_with_oil_content.xlsx', index=False)
