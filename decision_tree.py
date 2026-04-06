# Import necessary libraries
# !pip install dtreeviz   # Run this separately in terminal if needed

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import dtreeviz

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

species_names = ['setosa', 'versicolor', 'virginica']
y_labels = [species_names[label] for label in y]

print("___________________________________________")

# Display the class labels
print("Class Labels (Species):")
print(y_labels)

print("___________________________________________")

# Create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = y_labels
print(df.head())

print("___________________________________________")

# Setosa data
setosa_data = df[df['target'] == 'setosa']
print("Data for 'Setosa':")
print(setosa_data.head(3))

print("___________________________________________")

# Versicolor data
versicolor_data = df[df['target'] == 'versicolor']
print("Data for 'Versicolor':")
print(versicolor_data.head(3))

print("___________________________________________")

# Virginica data
virginica_data = df[df['target'] == 'virginica']
print("Data for 'Virginica':")
print(virginica_data.head(3))

print("___________________________________________")

# Binary classification: virginica vs others
y_binary = (y == 2).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_binary, test_size=0.3, random_state=42
)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

print("___________________________________________")

# Visualization
viz = dtreeviz.model(
    clf,
    X_train,
    y_train,
    target_name='target',
    feature_names=data.feature_names,
    class_names=['virginica', 'versicolor']
)

viz.view()