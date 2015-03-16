from flask import Flask 
@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your brower if %s</p>' % user_agent