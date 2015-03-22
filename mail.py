#!-*-utf-8-*-

from flask import Flask, render_template

from flask.ext.mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 465
#app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USE_TLS'] = True

#app.config['MAIL_USERNAME'] = 'xxxxxx@126.com'
#app.config['MAIL_PASSWORD'] = 'xxxxxx'


app.config['MAIL_USERNAME'] = 'xxxxxx'
app.config['MAIL_PASSWORD'] = 'xxxxxx'

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <pythonweb@126.com>'
app.config['FLASKY_ADMIN'] = 'xxx@126.com' 

mail = Mail(app)

def send_email(to, subject):
	print 'the message is sending.......'
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
		sender = app.config['FLASKY_MAIL_SENDER'], recipients= [to])
	#msg.body = render_template(template + '.txt', **kwargs)
	#msg.html = render_template(template + '.html', **kwargs)
	msg.body = "this is a test"
	msg.html = "<b>this is a test</b>"
	print "sending..........."
	mail.send(msg)
	print "message has been sended"

with app.app_context():
	send_email(app.config['FLASKY_ADMIN'],'New User')

