from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load(os.path.join("models", "Food_Prediction_Complaint.joblib"))
preprocessor = joblib.load(os.path.join("models", "Preprocessor.joblib"))

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Complaint prediction page (GET for form, POST for result)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'driver_rating': float(request.form['driver_rating']),
                'food_type': request.form['food_type'],
                'weather_condition': request.form['weather_condition'],
                'packaging_type': request.form['packaging_type'],
                'customer_past_complaints': int(request.form['customer_past_complaints']),
                'city': request.form['city'],
                'delivery_duration': float(request.form['delivery_duration'])
            }

            # Validate input
            if data['driver_rating'] == 0 or data['delivery_duration'] == 0:
                raise ValueError("Driver rating and delivery duration cannot be 0.")
            if data['driver_rating'] > 5:
                raise ValueError("Driver rating cannot be greater than 5.")

            # Predict
            input_df = pd.DataFrame([data])
            processed_input = preprocessor.transform(input_df)
            prediction = model.predict(processed_input)[0]
            confidence = model.predict_proba(processed_input)[0][int(prediction)]

            result_text = "Complaint" if prediction == 1 else "No Complaint"

            return render_template('result.html',
                                   prediction=result_text,
                                   confidence=round(confidence * 100, 2))

        except Exception as e:
            return render_template('result.html', prediction="Error", confidence=str(e))

    # GET request: Show form
    return render_template('predict.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
