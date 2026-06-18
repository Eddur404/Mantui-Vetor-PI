from flask import render_template
from . import bp

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/avistamentos")
def avistamentos():
    aves = ["Arara", "Calidris Alba", "Maçarico Branco"]

    return render_template('avistamentos.html', aves=aves)

@bp.route("/sobre")
def sobre():
    return render_template('sobre.html')

@bp.route("/mapa")
def mapa():
    return render_template('mapa.html')

@bp.route("/contato")
def contato():
    return render_template('contato.html')