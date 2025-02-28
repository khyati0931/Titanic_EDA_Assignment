# -*- coding: utf-8 -*-
"""DAI Assignment_23113083

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/119ZZ2QB4M9iiVc_ZALH9VGcke1yGTML3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

print("Dataset Overview:")
print(df.info())
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
df.fillna({'Age': df['Age'].median(), 'Embarked': df['Embarked'].mode()[0]}, inplace=True)
df.drop(columns=['Cabin', 'Name', 'Ticket'], inplace=True)

"""UNIVARIATE ANALYSIS"""

df.hist(figsize=(12, 8), bins=30)
plt.suptitle("Univariate Analysis - Histograms")
plt.show()

categorical_cols = ['Sex', 'Embarked', 'Pclass']
for col in categorical_cols:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=df[col])
    plt.title(f"Count Plot for {col}")
    plt.xticks(rotation=45)
    plt.show()

"""MULTIVARIATE ANALYSIS"""

df_encoded = df.copy()
df_encoded['Sex'] = df_encoded['Sex'].map({'male': 0, 'female': 1})
df_encoded = pd.get_dummies(df_encoded, columns=['Embarked'], drop_first=True)

#correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Pairplot for numerical columns
if 'Survived' in df.columns:
    sns.pairplot(df, hue='Survived')
    plt.show()
else:
    print("Column 'Survived' not found in the dataset.")

# Survival rate by class
plt.figure(figsize=(6, 4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

# Survival rate by gender
plt.figure(figsize=(6, 4))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title("Survival Rate by Gender")
plt.show()

# Scatter plot for Fare vs. Age colored by Survival
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title("Fare vs. Age by Survival")
plt.show()

df.to_csv("titanic_analysis.csv", index=False)