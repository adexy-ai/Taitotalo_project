from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import webview


app = Flask(__name__)

# Sample data for training the model
data = {
    'population': [1000, 2000, 3000, 4000, 5000],
    'diabetes_cases': [50, 100, 150, 200, 250]
}

df = pd.DataFrame(data)

X = df[['population']]
y = df['diabetes_cases']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    population = int(request.form['population'])
    prediction = model.predict(np.array([[population]]))[0]
    return jsonify({'predicted_diabetes_cases': prediction})

@app.route("/")
def home_page():
    date_ = dt.datetime.now().year
    return render_template('index.html', year=date_)

@app.route("/projects")
def elements():
    return render_template('projects.html')

@app.route("/contacts")
def generic():
    return render_template('contacts.html')

@app.route("/form_entry", methods=['POST', 'GET'])
def recieve_data():
    name = request.form.get['name']
    email = request.form.get['email']
    message = request.form.get['message']
    return f'<h2>Name: {name}, Email: {email}, Message: {message}<h2/>'





if __name__ == '__main__':
    app.run(debug=True, port=5001)
    