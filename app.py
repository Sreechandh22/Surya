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
