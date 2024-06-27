from flask import Flask, render_template
import datetime as dt


app = Flask(__name__)

@app.route("/")
def home_page():
    date_ = dt.datetime.now().year
    return render_template('index.html', year=date_)


# @app.route("/about")
# def about():
#     return render_template('about.html')


@app.route("/projects")
def elements():
    return render_template('projects.html')


@app.route("/contacts")
def generic():
    return render_template('contacts.html')






if __name__ == '__main__':
    app.run()