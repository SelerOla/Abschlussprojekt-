from flask import Flask, send_from_directory
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def home():
    return '<h1>Welcome to the COVID Dashboard</h1> <img src="/static/covid_dashboard.png" alt="COVID Dashboard">'

@app.route('/static/<covid_dashboard>')
def send_image(covid_dashboard):
    return send_from_directory(app.config['UPLOAD_FOLDER'], covid_dashboard)

if __name__ == '__main__':
    app.run(debug=True)
