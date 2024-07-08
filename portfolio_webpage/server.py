from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Email, Length
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



app = Flask(__name__) 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///contacts.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

    
# create the table for the contact data server
class Contacts(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    message: Mapped[float] = mapped_column(String(1000), nullable=False)


# create table schema in the database
def create_schema():
    with app.app_context():
        db.create_all()

# call the function once and then comment it out once the db is created
create_schema()



@app.route("/contacts", methods=['POST', 'GET'])
def recieve_data():
    if request.method == "POST":
        contact_request = Contacts(
            name= request.form["name"],
            email= request.form["email"],
            message= request.form["message"]
        )
        db.session.add(contact_request)
        db.session.commit()
    
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home_page'))
      
    return render_template("contacts.html")

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




if __name__ == '__main__':
    app.run(debug=True, port=5001)
    