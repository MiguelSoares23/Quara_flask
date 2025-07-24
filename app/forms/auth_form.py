from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class CadastroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo('senha', message="Senhas devem coincidir")])

    tipo = SelectField("Tipo", choices=[
        ('usuario', 'Usuário'),
        ('doador', 'Doador')
    ], validators=[DataRequired()])  # usuario, admin ou doador

    submit = SubmitField("Cadastrar")