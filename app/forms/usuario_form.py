from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class UsuarioForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmar_senha = PasswordField("Confirmar senha", validators=[EqualTo("senha", "As senhas precisam ser iguais.")])
    tipo = SelectField("Tipo", choices=[('usuario', 'Usuário'), ('admin', 'Administrador')])
    submit = SubmitField("Criar Conta")
