import os
basedir = os.path.abspath(os.path.dirname(__file__))
# NOTE: temporary development config, REPLACE with separate dev/prod config during production

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'extremely-secret-key'
	# SQLAlchemy config
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False