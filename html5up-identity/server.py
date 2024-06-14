from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('html5up-identity/templates/index.html')




if __name__ == '__main__':
    app.run()