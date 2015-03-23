from flask import Flask, render_template
from flsak.ext.boostrap import Bootstrap
from flask.ex.mail import Mail 
from flask.ext.moment import Moment 
from flask.ext.sqlachemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):

	


	app = Flask(__name__)

	from .main import main as main_blueprint 
	app.register_blueprint(main_blueprint)


	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init(app)
	db.init_app(app)

	#add the route and deal_error html

	return app