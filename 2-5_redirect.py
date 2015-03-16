from flask import redirect

@app.route('/')
def index():
	return redirect('http://www.example.com')