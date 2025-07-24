from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import db, Usuario
from app.forms.usuario_form import UsuarioForm
from app.utils.decorators import login_requerido, admin_requerido

usuarios_bp = Blueprint('usuarios', __name__, url_prefix="/usuarios", template_folder="../templates/usuarios")

@usuarios_bp.route("/")
@login_requerido
@admin_requerido
def listar():
    usuarios = Usuario.query.all()
    return render_template("listar.html", usuarios=usuarios)

@usuarios_bp.route("/criar", methods=["GET", "POST"])
@login_requerido
@admin_requerido
def criar():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            senha=form.senha.data,  # hash recomendado
            tipo=form.tipo.data
        )
        db.session.add(usuario)
        db.session.commit()
        flash("Usuário criado com sucesso.", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("criar.html", form=form)

@usuarios_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_requerido
@admin_requerido
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.nome = form.nome.data
        usuario.email = form.email.data
        usuario.tipo = form.tipo.data
        db.session.commit()
        flash("Usuário atualizado com sucesso.", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("editar.html", form=form, usuario=usuario)

@usuarios_bp.route("/deletar/<int:id>", methods=["POST"])
@login_requerido
@admin_requerido
def deletar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash("Usuário deletado com sucesso.", "info")
    return redirect(url_for("usuarios.listar"))
