from flask import render_template
from app.base import blueprint


@blueprint.route('/')
def route_default():
    return render_template("index.html")