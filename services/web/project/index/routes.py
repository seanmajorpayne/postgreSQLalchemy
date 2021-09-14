from flask import jsonify
from project.index import bp


@bp.route("/")
@bp.route("/index")
def index():
    return jsonify(hello="world")
