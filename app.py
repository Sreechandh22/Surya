# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__, static_url_path='/static')


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     print("Received data:", data)  # Debug statement

#     # Initialize stress score
#     stress_score = 0

#     # Extract and validate data
#     gender = data.get('gender')

#     # Convert age to float
#     age_str = data.get('age')
#     try:
#         age = float(age_str) if age_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         age = None

#     # Convert BMI to float
#     bmi_str = data.get('bmi')
#     try:
#         bmi = float(bmi_str) if bmi_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         bmi = None

#     # Convert sleep time to float
#     sleep_time_str = data.get('sleepTime')
#     try:
#         sleep_time = float(sleep_time_str) if sleep_time_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         sleep_time = None

#     # Convert blood pressure to float
#     blood_pressure_str = data.get('bloodPressure')
#     try:
#         blood_pressure = float(blood_pressure_str) if blood_pressure_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         blood_pressure = None

#     # Convert heart rate to float
#     heart_rate_str = data.get('heartRate')
#     try:
#         heart_rate = float(heart_rate_str) if heart_rate_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         heart_rate = None

#     # Convert steps walked to float
#     steps_walked_str = data.get('stepsWalked')
#     try:
#         steps_walked = float(steps_walked_str) if steps_walked_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         steps_walked = None

#     # Calculate stress score based on various factors
#     if age is not None:
#         if age < 30:
#             stress_score += 10
#         elif age >= 30 and age < 50:
#             stress_score += 20
#         else:
#             stress_score += 30

#     if bmi is not None:
#         if bmi < 18.5:
#             stress_score += 20
#         elif bmi >= 25:
#             stress_score += 10

#     if sleep_time is not None:
#         if sleep_time < 6:
#             stress_score += 20
#         elif sleep_time < 8:
#             stress_score += 10

#     if blood_pressure is not None:
#         if blood_pressure > 140:
#             stress_score += 30
#         elif blood_pressure > 120:
#             stress_score += 20

#     if heart_rate is not None:
#         if heart_rate > 100:
#             stress_score += 20
#         elif heart_rate > 80:
#             stress_score += 10

#     if steps_walked is not None:
#         if steps_walked < 5000:
#             stress_score += 10

#     # Determine stress level based on the final score
#     if stress_score >= 60:
#         stress_level = "High"
#     elif stress_score >= 30:
#         stress_level = "Medium"
#     else:
#         stress_level = "Low"

#     # Placeholder values for Mood and Depression Risk
#     mood = "Happy"
#     depression_risk = "Low"

#     return_data = jsonify({"stressLevel": stress_level, "mood": mood, "depressionRisk": depression_risk})
#     print("Sending data:", return_data.json)  # Debug statement
#     return return_data

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    gender = data.get('gender')
    age = data.get('age')
    bmi = data.get('bmi')
    sleepTime = data.get('sleepTime')
    bloodPressure = data.get('bloodPressure')
    heartRate = data.get('heartRate')
    stepsWalked = data.get('stepsWalked')

    stress_score = 0
    mood = ''
    depressionRisk = ''

    # Full-scale logic for prediction
    if gender == 'male':
        stress_score += 1
    else:
        stress_score += 2

    if age == '18-30':
        stress_score += 1
    elif age == '31-45':
        stress_score += 2
    else:
        stress_score += 3

    if bmi == 'underweight':
        stress_score += 3
    elif bmi == 'normal':
        stress_score += 1
    else:
        stress_score += 2

    if sleepTime == 'less-than-6':
        stress_score += 3
    elif sleepTime == '6-7':
        stress_score += 2
    else:
        stress_score += 1

    if bloodPressure == 'normal':
        stress_score += 1
    else:
        stress_score += 2

    if heartRate == 'normal':
        stress_score += 1
    else:
        stress_score += 2

    if stepsWalked == 'less-than-5000':
        stress_score += 3
    elif stepsWalked == '5000-10000':
        stress_score += 2
    else:
        stress_score += 1

    if stress_score <= 10:
        mood = 'Happy'
        depressionRisk = 'Low'
    elif stress_score <= 15:
        mood = 'Neutral'
        depressionRisk = 'Medium'
    else:
        mood = 'Sad'
        depressionRisk = 'High'

    return jsonify({'mood': mood, 'depressionRisk': depressionRisk})

if __name__ == '__main__':
    app.run(debug=True)