from app import db
from datetime import datetime


class Roupa(db.Model):
    __tablename__ = 'roupas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    tamanho = db.Column(db.String(10))
    tipo = db.Column(db.String(20))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(200))  # Caminho para o arquivo
    categoria = db.Column(db.String(10))  # 'venda' ou 'doacao'
    status = db.Column(db.String(20), default='disponivel')

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    venda = db.relationship('Venda', backref='roupa', uselist=False)
    doacao = db.relationship('Doacao', backref='roupa', uselist=False)