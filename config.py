import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	
	FLASKY_MAIL_SENDER = 'Flasky Admin <pythonweb@126.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	FLASKY_POSTS_PER_PAGE = 20
	FLASKY_FOLLOWERS_PER_PAGE = 50
	FLASKY_COMMENTS_PER_PAGE = 30

	MAIL_SERVER = 'smtp.126.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USE_TLS = False
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
				'sqlit:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development' : DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
}