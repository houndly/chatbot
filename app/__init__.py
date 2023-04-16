"""
	Module to init Flask application configuration
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('app.config')

# Import routes to handle on Flask APP
from app import routes
