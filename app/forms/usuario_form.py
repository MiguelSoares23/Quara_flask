from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha")  # só exige ao criar
    tipo = SelectField("Tipo", choices=[("admin", "Administrador"), ("vendedor", "Doador"), ("usuario", "Usuário")])
    submit = SubmitField("Salvar")
