import os
# NOTE: temporary development config, REPLACE with separate dev/prod config during production

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'extremely-secret-key'