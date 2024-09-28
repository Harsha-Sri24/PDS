# -*- coding: utf-8 -*-
"""Clean_data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vEY7CELEH27kam8yG5NAhp_78j3oGlp5
"""

from google.colab import files
import pandas as pd
from scipy import stats

# Step 1: Upload the file
uploaded = files.upload()

# Step 2: Load the data into a DataFrame
df = pd.read_csv('StudentsPerformance.csv')

# Display the first few rows
print(df.head())

print("Missing Values in Dataset:")
print(df.isnull().sum())


# 1.2 Checking for duplicates
print("Number of Duplicates in the dataset:", df.duplicated().sum())

#Finding Outliers
z_scores = stats.zscore(df[['math score', 'reading score', 'writing score']])
abs_z_scores = abs(z_scores)
outliers = (abs_z_scores > 3).any(axis=1)

print("Outliers based on Z-score:")
print(df[outliers])

#Saving the cleaned data to a csv file
df.to_csv('cleaned_student_data.csv', index=False)
print("File downloaded successfully")