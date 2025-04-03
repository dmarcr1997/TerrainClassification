from flask import Flask, render_template, request # import flask and render template
from model import load_model # to load model

# Create new flask app with its name as application module's name
app = Flask(__name__) 
model = load_model("terrain_classification.pkl") # load model 

@app.route('/') # base route
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data from user input form
    motor_current = float(request.form['motor_current'])
    vibration = float(request.form['vibration'])
    slip = float(request.form['slip'])
    incline = float(request.form['incline'])
    obstacle = float(request.form['obstacle'])

    # Create feature array to pass into model
    features = [[motor_current, vibration, slip, incline, obstacle]]
    
    # Make prediction based on input to model
    prediction = model.predict(features)[0]

    # Show result on the page
    return render_template('index.html', prediction=prediction)