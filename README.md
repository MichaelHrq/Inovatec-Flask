Abra a pasta do projeto no cmd e escreva:

- pip install virtualenv
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt

Criar um arquivo na raiz chamado ".flaskenv" e cole as seguintes linhas:
- FLASK_APP="app/__init__.py"
- FLASK_RUN_PORT=8080

Criando o DB :
- flask db init
- flask db migrate
- flask db upgrade

E por fim, digite:
- flask run
