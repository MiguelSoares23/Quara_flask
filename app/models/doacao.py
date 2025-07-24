from app import db
from datetime import datetime

class Doacao(db.Model):
    __tablename__ = 'doacoes'
    id = db.Column(db.Integer, primary_key=True)
    roupa_id = db.Column(db.Integer, db.ForeignKey('roupas.id'), nullable=False)
    doador_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data_doacao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pendente')  # 'pendente', 'aprovada', 'recusada'