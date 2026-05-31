import pandas as pd

# Load Excel dataset
df = pd.read_excel("Customer_Personality_Analysis_5000.xlsx")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Standardize text columns
df['gender'] = df['gender'].str.title()
df['country'] = df['country'].str.title()
df['education'] = df['education'].str.title()
df['marital_status'] = df['marital_status'].str.title()

# Convert date column
df['dt_customer'] = pd.to_datetime(
    df['dt_customer'],
    format='%d-%m-%Y',
    errors='coerce'
)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check for duplicates after cleaning
print("\nDuplicate Rows:", df.duplicated().sum())

# Final missing value check
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_excel("Cleaned_Customer_Personality_Analysis.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned file saved as 'Cleaned_Customer_Personality_Analysis.xlsx'")