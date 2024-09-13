from database import db
class Lojas(db.Model):
    __tablename__="lojas"
    id_loja = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    telefone = db.Column(db.String(15))

    def __init__(self, nome,endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone 

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)