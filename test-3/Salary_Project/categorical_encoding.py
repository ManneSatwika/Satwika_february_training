import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

df = pd.read_csv(r'C:\Users\SAKSHITHA\OneDrive\Desktop\archieve\Salary_Data\Salary_Data.csv')

cat_cols = df.select_dtypes(exclude=np.number).columns

print("Categorical columns:", cat_cols)

df_onehot = pd.get_dummies(df, columns=cat_cols)
print("One Hot Encoding done")

label = LabelEncoder()
df_label = df.copy()
for col in cat_cols:
    df_label[col] = label.fit_transform(df_label[col])
print("Label Encoding done")

ordinal = OrdinalEncoder()
df_ordinal = df.copy()
df_ordinal[cat_cols] = ordinal.fit_transform(df_ordinal[cat_cols])
print("Ordinal Encoding done")

df_freq = df.copy()
for col in cat_cols:
    freq = df_freq[col].value_counts()
    df_freq[col] = df_freq[col].map(freq)
print("Frequency Encoding done")

df_target = df.copy()
for col in cat_cols:
    target_mean = df_target.groupby(col)["Salary"].mean()
    df_target[col] = df_target[col].map(target_mean)
print("Target Encoding done")

print(df_onehot.head())
print(df_label.head())
print(df_ordinal.head())
print(df_freq.head())
print(df_target.head())