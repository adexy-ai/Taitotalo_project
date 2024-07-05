from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import webview
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Email, Length
import csv


app = Flask(__name__) 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Creating the form function to get the import from the form page of the website

class Message_Ade(FlaskForm):
    name = StringField('NAME', validators=[DataRequired()])
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    message = StringField('MESSAGE', validators=[DataRequired(), Length(min=2, max=150)])
    submit = SubmitField('SEND MESSAGE')


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
    prediction = round(model.predict(np.array([[population]]))[0])
    return jsonify({'predicted_diabetes_cases': prediction})

@app.route("/")
def home_page():
    date_ = dt.datetime.now().year
    return render_template('index.html', year=date_)

@app.route("/projects")
def elements():
    return render_template('projects.html')

@app.route("/contacts", methods=['POST', 'GET'])
def generic():
    form = Message_Ade()
    if form.validate_on_submit():
        with open("messages.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.name.data},"
                           f"{form.email.data},)
                           f"{form.message.data},") 
    return render_template('contacts.html', form=form)

@app.route("/form_entry", methods=['POST', 'GET'])
def recieve_data():
    form = Message_Ade()
    if form.validate_on_submit():
        with open("messages.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.name.data},"
                           f"{form.email.data},"
                           f"{form.message.data},")  
        return render_template('footer.html', form=form)






if __name__ == '__main__':
    app.run(debug=True, port=5001)
    