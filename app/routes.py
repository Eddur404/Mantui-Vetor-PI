from flask import render_template
from . import bp

@bp.route("/")
def login():
    render_template('index.html')