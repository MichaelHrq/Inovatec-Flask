from flask import request
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        nome = data['nome']
        senha = data['senha']
        user = User.query.filter_by(nome=nome).first()
        if (not user) or (not user.ConfirmarSenha(senha)) : 
            return 'Login ou senha invalido', 500
        login_user(user)
        return 'Login efetivado'

    except Exception as e:
        return 'Erro interno do servidor: {}'.format(e), 500


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()

@app.route('/register', methods=['POST'])
def register():
    try :
        data = request.get_json()
        nome = data['nome']
        email = data['email']
        senha = data['senha']

        user = User(nome,email,senha)
        db.session.add(user)
        db.session.commit()

        return 'Cadastro efetivado'
    
    except Exception as e:
        return 'Erro interno do servidor: {}'.format(e), 500



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)