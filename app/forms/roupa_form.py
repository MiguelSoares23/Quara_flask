from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired

class RoupaForm(FlaskForm):
    nome = StringField('Nome da Roupa', validators=[DataRequired()])
    descricao = TextAreaField('Descrição')
    
    tamanho = SelectField('Tamanho', choices=[
        ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')
    ], validators=[DataRequired()])

    tipo = SelectField('Tipo', choices=[
        ('masculina', 'Masculina'),
        ('feminina', 'Feminina'),
        ('infantil', 'Infantil'),
        ('outro', 'Outro')
    ])

    preco = FloatField('Preço', validators=[DataRequired()])
    
    imagem = FileField('Imagem da Roupa')  # Implementação do upload será feita na rota
    
    categoria = SelectField('Categoria', choices=[
        ('venda', 'Venda'),
        ('doacao', 'Doação')
    ], validators=[DataRequired()])

    submit = SubmitField('Salvar')
