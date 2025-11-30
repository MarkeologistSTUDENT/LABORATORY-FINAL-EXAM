import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

BASE = Path(__file__).resolve().parent
CSV = BASE / 'faculty_workload.csv'
MODEL_OUT = BASE / 'stress_model.joblib'

def load_data(path=CSV):
    df = pd.read_csv(path)
    return df

def prepare(df):
    X = df[['Subjects_Handled','Students_Total','Prep_Hours','Research_Load_Hours','Committee_Duties','Admin_Tasks','Meeting_Hours','Sleep_Hours','Weekend_Work']]
    y = df['Stress_Level']
    return X, y

def train_and_save(path=CSV, out=MODEL_OUT):
    df = load_data(path)
    X, y = prepare(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))
    joblib.dump(clf, out)
    print(f"Saved model to {out}")

if __name__ == '__main__':
    train_and_save()
