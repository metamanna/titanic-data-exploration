import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme(style='whitegrid', palette='Set2', font_scale=1.2)
import matplotlib.pyplot as plt

# import os
# file_path = r'E:\Celebal project\Assignment3\archive (1)\Titanic-Dataset.csv'
# print("Exists:", os.path.exists(file_path))
df = pd.read_csv(r'E:\Celebal project\Assignment3\archive (1)\Titanic-Dataset.csv')
print(df.head(3))
df.info()
df.describe()
#replace empty values with NaN
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
print(df.isnull().sum().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
df.drop(columns='Cabin', inplace=True)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(df.isnull().sum().sum())

# 🔹 Extract Title from Name
df['Title'] = df['Name'].str.extract(r'([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'], 'Rare')
df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

# 🔹 Create Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

survival_counts = df['Survived'].value_counts()
plt.pie(survival_counts, labels=['Did not survive', 'Survived'], autopct='%1.1f%%', startangle=90, colors=['#ff6f69', '#88d8b0'])
plt.title('Survival Rate')
plt.gca().add_artist(plt.Circle((0,0), 0.3, color='white'))  # Donut effect
plt.axis('equal')
plt.show()

sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True, palette='pastel')
plt.title('Age and Class Impact on Survival')
plt.show()

g = sns.FacetGrid(df, col="Pclass", height=4, hue="Survived", palette="Set2")
g.map(sns.histplot, "Age", bins=20, kde=True)
g.add_legend()
g.fig.suptitle("Age Distribution by Class and Survival", y=1.05)
plt.show()