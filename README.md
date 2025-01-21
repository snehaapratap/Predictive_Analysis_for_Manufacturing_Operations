# Predictive Analysis for Manufacturing Operations

This repository contains a RESTful API for predictive analysis in manufacturing, focusing on machine downtime and production defects. It includes:
- Data generation (using `data.py`).
- A supervised machine learning model trained with scikit-learn.
- Flask-based endpoints for data upload, training, and prediction.

This project demonstrates proficiency in Python, REST API development, and machine learning for practical applications.

---

## **Features**
- **Dynamic Dataset**: A synthetic dataset can be generated using `data.py` for customization and testing.
- **Supervised ML Model**: Uses logistic regression to predict machine downtime or defects.
- **RESTful API**: Includes endpoints to:
  - Upload manufacturing data.
  - Train the ML model.
  - Predict outcomes based on input data.

---

## **File Structure**
```
Predictive_Analysis_For_Manufacturing/
│
├── app.py                                     # Flask application with RESTful API endpoints
├── data.py                                    # Script to generate synthetic manufacturing data
├── synthetic_manufacturing_data.csv           # Example dataset
├── requirements.txt                           # Python dependencies
├── README.md                                  # Documentation
└── venv/                                      # Virtual environment 
```

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.7 or above
- pip (Python package manager)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/snehaapratap/Predictive_Analysis_For_Manufacturing_Operations.git
   cd Predictive_Analysis_For_Manufacturing_Operations
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Generate a synthetic dataset:
   ```bash
   python data.py
   ```
   This will create a file named `synthetic_manufacturing_data.csv`.

---

## **How to Run the API**
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. The API will be available at: `http://127.0.0.1:5000/`.

---

## **API Endpoints**

### **1. Upload Data**
- **URL**: `POST /upload`
- **Description**: Upload a CSV file with manufacturing data.
- **Input**: CSV file (form-data key: `file`).
- **Response**:
  ```json
  {
    "message": "File uploaded successfully"
  }
  ```

### **2. Train Model**
- **URL**: `POST /train`
- **Description**: Train the ML model on uploaded data.
- **Response**:
  ```json
  {
    "accuracy": 0.89,
    "f1_score": 0.0
  }
  ```

### **3. Predict**
- **URL**: `POST /predict`
- **Description**: Predict machine downtime based on input.
- **Input**:
  ```json
  {
    "Temperature": 80,
    "Run_Time": 120
  }
  ```
- **Response**:
  ```json
  {
    "Downtime": "No",
    "Confidence": 0.85
  }
  ```

---

## **Testing the API Locally**
1. Use Postman or `cURL` to test the endpoints:
   - **Upload Data**: Attach the `synthetic_manufacturing_data.csv`.
   - **Train Model**: Send a `POST` request to `/train`.
   - **Predict**: Send JSON input to `/predict`.

2. Example `cURL` command for prediction:
   ```bash
   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_Time": 120}'
   ```

---

## **Technologies Used**
- **Backend Framework**: Flask
- **Machine Learning**: scikit-learn
- **Language**: Python
- **Dataset**: Synthetic manufacturing data

---

## **Skills Demonstrated**
- **REST API Development**: Created a robust API with Flask.
- **Machine Learning**: Applied logistic regression to real-world manufacturing data.
- **Data Generation**: Generated synthetic datasets for testing.
- **Documentation**: Provided clear setup instructions and endpoint details.

---

## **Future Improvements**
- Expand dataset generation to include more features and variability.
- Add support for additional machine learning models.
- Enhance API with authentication and input validation.

---

Let me know if you need further adjustments or enhancements!
