from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id).first()

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email,senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def ConfirmarSenha(self, senha):
        return check_password_hash(self.senha, senha)