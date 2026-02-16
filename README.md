# 🍔 Food Complaint Prediction System

An end-to-end Machine Learning project that predicts whether a food delivery order is likely to result in a customer complaint.

This system analyzes order details, delivery performance, and customer-related features to proactively identify high-risk orders. It helps businesses improve service quality, reduce complaints, and enhance customer satisfaction.

---

# 📌 Problem Statement

Food delivery platforms often receive complaints due to:

- Late delivery
- Incorrect items
- Poor packaging
- Service quality issues

Instead of reacting after a complaint occurs, this system predicts complaints in advance so businesses can take preventive action.

---

# 🎯 Project Objectives

- Predict customer complaints using Machine Learning
- Handle class imbalance effectively
- Compare multiple ML algorithms
- Select best-performing model
- Deploy model using Flask
- Create an interactive, food-themed UI

---

# 🛠️ Technologies & Tools Used

## Programming Language
- Python

## Data Processing
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)

## Data Visualization (EDA)
- Matplotlib
- Seaborn

## Machine Learning Models Implemented
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier
- Gradient Boosting Classifier

## Deployment
- Flask (Backend)
- HTML
- CSS (Animated UI)
- Joblib (Model Persistence)

---

# 📊 Machine Learning Pipeline

## 1️⃣ Data Collection

Dataset includes:
- Order details
- Delivery time
- Pricing
- Customer ratings
- Order conditions
- Complaint label (Target variable)

---

## 2️⃣ Data Preprocessing

✔ Handling missing values  
✔ Removing duplicates  
✔ Encoding categorical variables  
✔ Feature scaling (Standardization / Normalization)  
✔ Feature selection  
✔ Train-test split  

---

## 3️⃣ Handling Class Imbalance

Complaint datasets are usually imbalanced.

To solve this:
- Applied SMOTE (Synthetic Minority Oversampling Technique)
- Balanced minority complaint class
- Improved recall and model stability

---

## 4️⃣ Model Training & Comparison

Multiple classification models were trained and evaluated:

| Model | Accuracy | Observation |
|-------|----------|------------|
| Logistic Regression | Moderate | Linear baseline model |
| Decision Tree | Good | Prone to overfitting |
| Random Forest | Very Good | Reduced variance |
| XGBoost | High | Strong boosting performance |
| **Gradient Boosting** | **Highest Accuracy** | Best overall performance |

---

## 🏆 Best Performing Model

### Gradient Boosting Classifier

- Achieved highest accuracy
- Balanced Precision and Recall
- Reduced overfitting compared to Decision Tree
- Strong generalization capability

Final selected model for deployment: **Gradient Boosting**

---

## 📈 Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Focus was placed on Recall and F1-Score due to class imbalance.

---

## 💾 Model Saving

Model saved using Joblib:

```python
import joblib
joblib.dump(model, "food_complaint_model.pkl")
```

Scaler and preprocessing objects were also saved to ensure consistent predictions.

---

## 🚀 Deployment (Flask Web Application)

### Application Flow:

1. User enters order details
2. Input is preprocessed using saved scaler & encoder
3. Gradient Boosting model predicts complaint probability
4. Result displayed on animated food-themed UI

---

# 📁 Project Structure

```
Food-Complaint-Prediction/
│
├── data/
├── notebooks/
├── static/
│   ├── css/
│   ├── images/
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   ├── result.html
│
├── app.py
├── food_complaint_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

# 🧠 How the Model Works

- The model learns historical complaint patterns.
- Boosting models sequentially correct previous errors.
- Gradient Boosting builds trees step-by-step to reduce loss.
- Final output gives probability of complaint occurrence.

Prediction Output:
- Complaint Likely
- No Complaint

---

# 📈 Business Impact

- Enables proactive complaint handling
- Reduces customer dissatisfaction
- Improves operational efficiency
- Supports data-driven decisions

---

# 🔮 Future Improvements

- Add Explainable AI (SHAP / LIME)
- Deploy on Cloud (AWS / Render / Heroku)
- Add analytics dashboard
- Integrate real-time tracking data
- Hyperparameter tuning with GridSearchCV

---

# 🧪 How to Run This Project

## Step 1: Clone Repository

```
git clone https://github.com/your-username/food-complaint-prediction.git
```

## Step 2: Navigate to Folder

```
cd food-complaint-prediction
```

## Step 3: Install Dependencies

```
pip install -r requirements.txt
```

## Step 4: Run Flask App

```
python app.py
```

## Step 5: Open in Browser

```
http://127.0.0.1:5000/
```

---

# 👨‍💻 Author

Sahil Suryavanshi  
Bachelor’s in Information Technology Engineering  
Aspiring AI / ML Engineer  
Passionate about building real-world ML systems  

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
