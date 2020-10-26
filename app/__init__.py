from flask import Flask
from app.search import engine

app = Flask(__name__)
engine.init()

from app import views
