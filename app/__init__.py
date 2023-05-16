"""
	Module to init Flask application configuration
"""

from flask import Flask
import app.config as config

app = Flask(__name__)
app.config.from_object(config)
app.config["SECRET_KEY"] = "secret_key"

# Import routes to handle on Flask APP
from app import routes
