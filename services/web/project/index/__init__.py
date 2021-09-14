from flask import Blueprint

bp = Blueprint("index", __name__)

from project.index import routes
