from database import db

class Equipamentos(db.Model):
    __tablename__ = "equipamentos"
    id_equipamento = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    codigo = db.Column(db.Integer)
    data_aquisicao = db.Column(db.Date)

    def __init__(self, nome, codigo, data_aquisicao):
        self.nome = nome
        self.codigo = codigo
        self.data_aquisicao = data_aquisicao

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)