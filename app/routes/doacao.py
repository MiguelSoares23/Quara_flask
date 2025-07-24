from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models.roupa import Roupa
from app.models.doacao import Doacao
from app.models.usuario import Usuario

doacoes_bp = Blueprint("doacoes", __name__, url_prefix="/doacoes")

@doacoes_bp.route("/nova/<int:roupa_id>", methods=["GET", "POST"])
def nova_doacao(roupa_id):
    if "usuario_id" not in session:
        flash("Você precisa estar logado para doar.", "danger")
        return redirect(url_for("auth.login"))

    if session.get("usuario_tipo") != "doador":
        flash("Apenas doadores podem realizar doações.", "danger")
        return redirect(url_for("main.home"))

    roupa = Roupa.query.get_or_404(roupa_id)

    if request.method == "POST":
        nova = Doacao(
            roupa_id=roupa.id,
            doador_id=session["usuario_id"],
            status="pendente"
        )
        db.session.add(nova)
        db.session.commit()
        flash("Doação registrada com sucesso! Aguarde aprovação.", "success")
        return redirect(url_for("main.home"))

    return render_template("doacoes/nova.html", roupa=roupa)

@doacoes_bp.route("/listar")
def listar_doacoes():
    if "usuario_id" not in session or session.get("usuario_tipo") != "admin":
        flash("Acesso restrito ao administrador.", "danger")
        return redirect(url_for("main.home"))

    doacoes = Doacao.query.all()
    return render_template("doacoes/listar.html", doacoes=doacoes)

@doacoes_bp.route("/aprovar/<int:id>")
def aprovar_doacao(id):
    doacao = Doacao.query.get_or_404(id)
    doacao.status = "aprovada"
    db.session.commit()
    flash("Doação aprovada.", "success")
    return redirect(url_for("doacoes.listar_doacoes"))

@doacoes_bp.route("/recusar/<int:id>")
def recusar_doacao(id):
    doacao = Doacao.query.get_or_404(id)
    doacao.status = "recusada"
    db.session.commit()
    flash("Doação recusada.", "warning")
    return redirect(url_for("doacoes.listar_doacoes"))
