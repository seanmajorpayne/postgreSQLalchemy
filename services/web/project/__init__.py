from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
Migrate(app, db)

from project.index import bp as index_bp
app.register_blueprint(index_bp)

from project import models