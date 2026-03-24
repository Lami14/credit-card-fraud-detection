import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('data/transactions.csv')

# Convert categorical variables using one-hot encoding
df = pd.get_dummies(df, columns=['location', 'card_type', 'merchant_category'])

# Features and target
X = df.drop(['transaction_id', 'time', 'is_fraud'], axis=1)
y = df['is_fraud']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open('model/fraud_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Fraud detection model trained and saved!")
