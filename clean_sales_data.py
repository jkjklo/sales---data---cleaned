import pandas as pd
import numpy as np

# Load the data (replace with your actual filename if needed)
df = pd.read_excel("sales-data-raw.xlsx", sheet_name="Sales_data")

# Remove unused or empty columns
if 'Column1' in df.columns:
    df = df.drop(columns=['Column1'])

# Standardize column names: lowercase, no spaces
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Remove duplicated rows
df = df.drop_duplicates()

# Handle missing values
df['salesperson'] = df['salesperson'].fillna('Unknown')
df['amount'] = df['amount'].replace('', np.nan).fillna('0')
df['product'] = df['product'].fillna('Unknown')
df['region'] = df['region'].fillna('Unknown')

# Clean and convert Amount
df['amount'] = df['amount'].astype(str).replace({'\$|,': ''}, regex=True)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0).astype(int)

# Normalize text columns
df['salesperson'] = df['salesperson'].str.strip().str.title()
df['product'] = df['product'].str.strip().str.title()
df['region'] = df['region'].str.strip().str.title()

# Fix and unify date formats as dd-mm-yyyy
df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=False)
df['date'] = df['date'].dt.strftime('%d-%m-%Y')

# Optional: re-order columns for clarity
df = df[['orderid', 'date', 'salesperson', 'amount', 'product', 'region']]

# Save cleaned data
df.to_excel("sales_data_cleaned.xlsx", index=False)
df.to_csv("sales_data_cleaned.csv", index=False)

print("Cleaning complete! Files saved as sales_data_cleaned.xlsx and sales_data_cleaned.csv.")
