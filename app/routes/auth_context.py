from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.forms.auth_form import LoginForm, CadastroForm
from app.models import Usuario, db

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

@auth_bp.route('/cadastro', methods=['GET','POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        if Usuario.query.filter_by(email=form.email.data).first():
            flash("E-mail já cadastrado.", "danger")
            return redirect(url_for('auth.cadastro'))

        novo_usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            tipo=form.tipo.data  # usuario ou doador
        )
        novo_usuario.set_senha(form.senha.data)

        db.session.add(novo_usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html', form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            session["usuario_id"] = usuario.id
            session["usuario_tipo"] = usuario.tipo
            flash("Login Bem-Sucedido!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("E-mail ou senha inválidos.", "danger")
    return render_template("auth/login.html", form=form)


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Usuário desconectado.", "info")
    return redirect(url_for('auth.login'))
