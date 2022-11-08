from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# initialize flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# setup loginManger, associate login handler view
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models