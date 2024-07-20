import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(url)

# Display the first few rows of the dataset
print(titanic_data.head())

# Display basic information about the dataset
print(titanic_data.info())

# Display summary statistics for the dataset
print(titanic_data.describe(include='all'))

# Check for missing values
print(titanic_data.isnull().sum())

# Fill missing values in 'Age' with the median age
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Fill missing values in 'Embarked' with the mode
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

# Drop the 'Cabin' column due to a large number of missing values
titanic_data.drop('Cabin', axis=1, inplace=True)

# Verify that there are no more missing values
print(titanic_data.isnull().sum())

# Survival rate based on gender
gender_survival_rate = titanic_data.groupby('Sex')['Survived'].mean()
print(f"Survival Rate by Gender:\n{gender_survival_rate}\n")

# Survival rate based on class
class_survival_rate = titanic_data.groupby('Pclass')['Survived'].mean()
print(f"Survival Rate by Class:\n{class_survival_rate}\n")

# Survival rate based on age groups
age_bins = [0, 12, 18, 35, 60, 120]
age_labels = ['Child', 'Teen', 'Adult', 'Middle-Aged', 'Senior']
titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_bins, labels=age_labels)
age_group_survival_rate = titanic_data.groupby('AgeGroup')['Survived'].mean()
print(f"Survival Rate by Age Group:\n{age_group_survival_rate}\n")

# Visualization

# Survival rate based on gender
plt.figure(figsize=(10, 5))
sns.barplot(x=gender_survival_rate.index, y=gender_survival_rate.values)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()

# Survival rate based on class
plt.figure(figsize=(10, 5))
sns.barplot(x=class_survival_rate.index, y=class_survival_rate.values)
plt.title('Survival Rate by Class')
plt.ylabel('Survival Rate')
plt.xlabel('Class')
plt.show()

# Survival rate based on age groups
plt.figure(figsize=(10, 5))
sns.barplot(x=age_group_survival_rate.index, y=age_group_survival_rate.values)
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate')
plt.xlabel('Age Group')
plt.show()
