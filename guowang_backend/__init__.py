from flask import Flask

app = Flask(__name__)

from guowang_backend import controller, models
