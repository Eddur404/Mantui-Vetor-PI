from flask import render_template, request, session, redirect, url_for
from . import bp

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        session["usuario"] = email

        return redirect(url_for('main.index'))
    
    return render_template('auth/login.html')


@bp.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')


        session["usuário"] = nome
        session["email"] = email


        return redirect(url_for('main.index'))
    
    return render_template('auth/registrar.html')

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('main.index'))