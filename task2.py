import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic Dataset
df = pd.read_csv("train.csv")

# ---------------------------
# Data Cleaning
# ---------------------------

print("Dataset Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column
df.drop('Cabin', axis=1, inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ---------------------------
# Dataset Information
# ---------------------------

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

sns.set_style("whitegrid")

# ---------------------------
# Passenger ID Distribution
# ---------------------------

plt.figure(figsize=(8,5))
plt.hist(df['PassengerId'], bins=30)
plt.title('Passenger ID Distribution')
plt.xlabel('Passenger ID')
plt.ylabel('Frequency')
plt.show()

# ---------------------------
# Survival Distribution
# ---------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title('Survival Distribution')
plt.show()

# ---------------------------
# Gender Distribution
# ---------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', data=df)
plt.title('Gender Distribution')
plt.show()

# ---------------------------
# Survival by Gender
# ---------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()

# ---------------------------
# Passenger Class Distribution
# ---------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', data=df)
plt.title('Passenger Class Distribution')
plt.show()

# ---------------------------
# Survival by Passenger Class
# ---------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Passenger Class')
plt.show()

# ---------------------------
# Age Distribution
# ---------------------------

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# ---------------------------
# Fare Distribution
# ---------------------------

plt.figure(figsize=(8,5))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.show()

# ---------------------------
# Age vs Fare
# ---------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(
    x='Age',
    y='Fare',
    hue='Survived',
    data=df
)
plt.title('Age vs Fare')
plt.show()

# ---------------------------
# Correlation Heatmap
# ---------------------------

numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10,6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)
plt.title('Correlation Heatmap')
plt.show()

# ---------------------------
# Insights
# ---------------------------

print("\nKey Insights:")
print("1. Female passengers had a higher survival rate.")
print("2. First-class passengers were more likely to survive.")
print("3. Most passengers were between 20 and 40 years old.")
print("4. Higher fare-paying passengers had better survival chances.")
print("5. PassengerId is only an identifier and does not affect survival.")