from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template('index.html')
