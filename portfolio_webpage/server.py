from flask import Flask, render_template
import datetime as dt


app = Flask(__name__)

@app.route("/")
def home_page():
    date_ = dt.datetime.now().year
    return render_template('index.html', year=date_)


@app.route("/about")
def about():
    return render_template('html5up-identity/templates/index.html')


@app.route("/projects")
def elements():
    return render_template('html5up-identity/templates/projects.html')


@app.route("/contacts")
def generic():
    return render_template('html5up-identity/templates/contacts.html')






if __name__ == '__main__':
    app.run()