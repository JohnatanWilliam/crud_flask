# verifico a pasta do meu projeto, verifico se esta no meu github
# git remote -v
# executar
# git pull origin master (main)




# pip install flask
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate
# pip install Flask-Script
# pip install pymsql

# flask db init
# flask db migrate -m "Migração Inicial"
# flask db upgrade

# flask run --debug




from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Lojas
app = Flask(__name__)
app.config['SECRET_KEY'] = 'J1J1x2x2x2a3a3a3a3'


# drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskzin2"

app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome='Maria', curso='Informatica', ano = 1):
    dados = {'nome': nome,'curso': curso, 'ano': ano}
    return render_template('aula.html',dados_html= dados)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    dados = request.form
    return render_template('dados.html', dados=dados)

@app.route('/usuario')
def usuario():
    u = Usuario.query.all()
    return render_template('usuario_lista.html', dados = u)



@app.route("/usuario/add")
def usuario_add():
    return render_template("usuario_add.html")


@app.route("/usuario/save", methods=['POST'])
def usuario_save():
    nome = request.form.get("nome")
    endereco = request.form.get("endereco")
    telefone = request.form.get("telefone")
    if nome and endereco and telefone:
        usuario = Lojas(nome,endereco,telefone)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario cadastrado com sucesso!')
        return redirect("/usuario")
    else:
        flash("preencha todos os campos!!!")
        return redirect("/usuario/add")


@app.route("/usuario/remove/<int:id_lojas>")
def usuario_remove(id_lojas):
    if id > 0:
        usuario = Lojas.query.get(id_lojas)
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuario removido com sucesso! :)")
        return redirect("/usuario")
    else:
        flash("Caminho incorreto!!!!!")
        return redirect("/usuario")


@app.route('/usuario/edita/<int:id_lojas>')
def usuario_edita(id_lojas):
    usuario = Lojas.query.get(id_lojas)
    return render_template('usuario_edita.html', dados = usuario)


@app.route('/usuario/editasave', methods=['POST'])
def usuario_editasave():
    id_lojas = request.form.get('id_lojas')
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    telefone = request.form.get('telefone')
    if id_lojas and nome and endereco and telefone:
        usuario = Lojas.query.get(id_lojas)
        usuario.nome = nome
        usuario.endereco = endereco
        usuario.telefone = telefone
        db.session.commit()
        flash('Dados atualizados com sucesso!!!')
        return redirect('/usuario')
    else:
        flash('Faltando dados!!!')
        return redirect('/usuario')



if __name__ == '__main__':
    app.run()
