import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler


def load_and_extract_features():
    """
    Feature dimensions based on the paper:
    Static: [File Source, Initial Path]
    Dynamic: [Integrity Measurement (Hash), Operation Behavior, ...]
    """

    np.random.seed(42)
    num_samples = 100000

    # 7-dimensional feature vectors
    X = np.random.rand(num_samples, 7)

    # Simulated labels: 'verified' (1) or 'none' (0)
    y = np.random.randint(0, 2, num_samples)

    return X, y



def train_random_forest(X, y):
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize Random Forest Classifier (30 trees based on paper)
    rf_model = RandomForestClassifier(n_estimators=30, random_state=42)

    # Cross-validation to find optimal parameters
    cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
    print(f"5-Fold CV Accuracy: {cv_scores.mean() * 100:.2f}%")

    # Train the model
    rf_model.fit(X_train, y_train)
    return rf_model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # The paper states an accuracy of over 99%
    print(f"Test Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    print("Loading dataset and extracting features...")
    X, y = load_and_extract_features()

    print("Training Random Forest model...")
    model, X_test, y_test = train_and_evaluate_model(X, y)

