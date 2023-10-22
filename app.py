# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json

#     # Initialize scores
#     stress_score = 0

#     # Extract and validate data
#     gender = data.get('gender')
#     age = data.get('age')

#     blood_pressure_str = data.get('bloodPressure')
#     try:
#         blood_pressure = int(blood_pressure_str) if blood_pressure_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         blood_pressure = None

#     sleep_time_str = data.get('sleepTime')
#     try:
#         sleep_time = int(sleep_time_str) if sleep_time_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         sleep_time = None

#     heart_rate_str = data.get('heartRate')
#     try:
#         heart_rate = int(heart_rate_str) if heart_rate_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         heart_rate = None

#     steps_walked_str = data.get('stepsWalked')
#     try:
#         steps_walked = int(steps_walked_str) if steps_walked_str.strip() != '' else None
#     except (ValueError, TypeError, AttributeError):
#         steps_walked = None

#     # Heuristic-based scoring
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

#     # Determine stress level based on score
#     if stress_score >= 60:
#         stress_level = "High"
#     elif stress_score >= 30:
#         stress_level = "Medium"
#     else:
#         stress_level = "Low"

#     return jsonify({"stressLevel": stress_level, "mood": "Happy", "depressionRisk": "Low"})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract and validate data
    age = data.get('age')
    bmi = data.get('bmi')
    sleep_quality = data.get('sleepQuality')
    stress_levels = data.get('stressLevels')
    physical_activity = data.get('physicalActivity')
    social_support = data.get('socialSupport')
    diet_quality = data.get('dietQuality')

    # Mood and Depression Prediction Algorithm
    mood_score = (
        age * 0.1 +
        bmi * 0.05 +
        sleep_quality * 0.1 -
        stress_levels * 0.15 +
        physical_activity * 0.1 +
        social_support * 0.15 +
        diet_quality * 0.1
    )

    depression_score = (
        age * 0.05 +
        bmi * 0.1 +
        sleep_quality * 0.1 +
        stress_levels * 0.15 -
        physical_activity * 0.1 -
        social_support * 0.1 -
        diet_quality * 0.1
    )

    # Determine mood and depression levels
    mood_level = "Happy" if mood_score >= 0 else "Sad"
    depression_level = "Low" if depression_score >= 0 else "High"

    return jsonify({"mood": mood_level, "depressionRisk": depression_level})

if __name__ == '__main__':
    app.run(debug=True)
