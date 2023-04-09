from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')

app.config['JWT_BLACKLIST_ENABLED'] =True
db = SQLAlchemy(app) 
migrate = Migrate(app,db)
jwt = JWTManager(app)

from app import models
from .api.apihandler import apiviews
app.register_blueprint(apiviews,url_prefix='/api')


@app.route('/')
def index():
    return "Hello World"
