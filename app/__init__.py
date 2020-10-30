from flask import Flask
from app.search import engine
from app.config import config_from_env

app = Flask(__name__)
engine.init()
config_from_env()

from app import views
