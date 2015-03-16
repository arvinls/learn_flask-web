@app.route('/')
def index():
	return '<h1>Bad Request</h1>', 400

#return object Response 
from flask import make_response

@app.route('/')
def index():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response
	