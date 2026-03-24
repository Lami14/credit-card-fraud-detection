from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model/fraud_model.pkl', 'rb'))

# Load original df for columns reference
df = pd.read_csv('data/transactions.csv')
columns_reference = pd.get_dummies(df, columns=['location', 'card_type', 'merchant_category']).drop(['transaction_id', 'time', 'is_fraud'], axis=1).columns

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Convert input to DataFrame
    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    # Add missing columns with 0
    for col in columns_reference:
        if col not in input_df:
            input_df[col] = 0
    input_df = input_df[columns_reference]  # ensure correct order
    prediction = model.predict(input_df)[0]
    result = "Fraudulent" if prediction == 1 else "Legitimate"
    return jsonify({'transaction_status': result})

if __name__ == '__main__':
    app.run(debug=True)
