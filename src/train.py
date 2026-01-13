import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, roc_auc_score

# 1. Config
DATA_PATH = 'churn.csv'
MODEL_PATH = 'models/churn_model.joblib'

def train():
    print("Loading data...")
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: File {DATA_PATH} not found. Please download dataset first.")
        return

    # Drop columns that are not useful for prediction
    # Adjust column names based on your specific CSV
    drop_cols = ['RowNumber', 'CustomerId', 'Surname']
    df = df.drop([c for c in drop_cols if c in df.columns], axis=1)

    X = df.drop('Exited', axis=1) # Target column is usually 'Exited' or 'Churn'
    y = df['Exited']

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 3. Define Preprocessing Pipeline
    # Numeric features
    numeric_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Categorical features
    categorical_features = ['Geography', 'Gender']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 4. Full Pipeline (Preprocessing + Model)
    # Using XGBoost
    clf = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42))
    ])

    # 5. Training
    print("Training model...")
    clf.fit(X_train, y_train)

    # 6. Evaluation
    print("Evaluating model...")
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)[:, 1]
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")

    # 7. Save Model
    joblib.dump(clf, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
