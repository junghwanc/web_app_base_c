from flask import Flask 
application = Flask(__name__)

@application.route('/')
def hello_world():
	return 'Welcome to Canada Web with EBS!!!!'