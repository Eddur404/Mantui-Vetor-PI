from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    senha_hash = db.Column(db.String(255), nullable = False)

    def set_senha_hash(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha_hash(self, senha):
        return check_password_hash(self.senha_hash, senha)