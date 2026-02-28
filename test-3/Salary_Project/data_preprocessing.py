import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, StandardScaler, Normalizer
df = pd.read_csv(r'C:\Users\SAKSHITHA\OneDrive\Desktop\archieve\Salary_Data\Salary_Data.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(exclude=np.number).columns

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print(df.isnull().sum())
df.to_csv("cleaned_salary_data.csv", index=False)
print("Cleaned dataset saved")