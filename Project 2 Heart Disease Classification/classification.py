"""
=========================================================
DecodeLabs Internship - Project 2
Project: Data Classification Using AI

Author: Rabeel Fatima

Dataset: heart.csv

Objective:
Predict whether a patient has heart disease using
Machine Learning (Random Forest Classifier)
=========================================================
"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ===============================
# Load Dataset
# ===============================

print("=" * 60)
print("HEART DISEASE CLASSIFICATION")
print("=" * 60)

data = pd.read_csv("heart.csv")

print("\nDataset Loaded Successfully!")


print("\nFirst Five Rows:\n")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(list(data.columns))

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# ===============================
# Features and Target
# ===============================

X = data.drop("target", axis=1)

y = data["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ===============================
# Train Model
# ===============================

print("\nTraining Model...\n")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Trained Successfully!")


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))


print("\nFeature Importance:\n")

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

for feature, value in importance.items():
    print(f"{feature:<12} : {value:.3f}")


print("\n" + "=" * 60)
print("NEW PATIENT PREDICTION")
print("=" * 60)

new_patient = pd.DataFrame([{
    "age": 52,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 230,
    "fbs": 0,
    "restecg": 1,
    "thalach": 170,
    "exang": 0,
    "oldpeak": 1.2,
    "slope": 2,
    "ca": 0,
    "thal": 2
}])

prediction = model.predict(new_patient)

print()

if prediction[0] == 1:
    print("Prediction: Patient HAS Heart Disease")
else:
    print("Prediction: Patient DOES NOT HAVE Heart Disease")

print("\nProject Completed Successfully!")
print("=" * 60)

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)

plt.title("Confusion Matrix")

plt.show()
