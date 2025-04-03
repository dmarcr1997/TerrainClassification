from flask import Flask, render_template # import flask and render template

# Create new flask app with its name as application module's name
app = Flask(__name__) 

@app.route('/') # base route
def index():
    return render_template('index.html')