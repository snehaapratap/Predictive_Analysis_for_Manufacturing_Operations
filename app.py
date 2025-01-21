from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)

model = None
uploaded_data = None  
@app.route('/upload', methods=['POST'])
def upload_data():
    """Upload manufacturing data as CSV"""
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    data = pd.read_csv(file)
    
    global uploaded_data
    uploaded_data = data
    
    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/train', methods=['POST'])
def train_model():
    """Train model on the uploaded dataset"""
    if uploaded_data is None:
        return jsonify({'error': 'No data uploaded'}), 400

    X = uploaded_data[['Temperature', 'Run_Time']]
    y = uploaded_data['Downtime_Flag']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    global model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return jsonify({'accuracy': accuracy, 'f1_score': f1}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Make prediction based on input data"""
    if model is None:
        return jsonify({'error': 'Model not trained yet'}), 400

    input_data = request.get_json()

    if 'Temperature' not in input_data or 'Run_Time' not in input_data:
        return jsonify({'error': 'Missing required fields'}), 400

    prediction = model.predict([[input_data['Temperature'], input_data['Run_Time']]])
    confidence = model.predict_proba([[input_data['Temperature'], input_data['Run_Time']]])[0][prediction[0]]

    return jsonify({'Downtime': 'Yes' if prediction[0] == 1 else 'No', 'Confidence': round(confidence, 2)})

if __name__ == '__main__':
    app.run(debug=True)
