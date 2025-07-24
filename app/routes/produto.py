from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import db, Roupa
from app.forms.roupa_form import RoupaForm

produtos = Blueprint('produtos', __name__, template_folder='../templates/produtos', url_prefix='/produtos')

@produtos.route('/')
def listar_roupas():
    roupas = Roupa.query.all()
    return render_template('lista_roupas.html', roupas=roupas)

@produtos.route('/adicionar', methods=['GET', 'POST'])
def adicionar_roupa():
    form = RoupaForm()
    if form.validate_on_submit():
        nova_roupa = Roupa(
            nome=form.nome.data,
            descricao=form.descricao.data,
            tamanho=form.tamanho.data,
            tipo=form.tipo.data,
            preco=form.preco.data,
            imagem="caminho/imagem.jpg",  # depois você implementa o upload
            categoria=form.categoria.data,
            usuario_id=1  # depois você usará o usuário logado (ex: session['usuario_id'])
        )
        db.session.add(nova_roupa)
        db.session.commit()
        flash('Roupa cadastrada com sucesso!', 'success')
        return redirect(url_for('produtos.listar_roupas'))
    return render_template('form_roupa.html', form=form)

@produtos.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_roupa(id):
    roupa = Roupa.query.get_or_404(id)
    form = RoupaForm(obj=roupa)
    if form.validate_on_submit():
        roupa.nome = form.nome.data
        roupa.descricao = form.descricao.data
        roupa.tamanho = form.tamanho.data
        roupa.tipo = form.tipo.data
        roupa.preco = form.preco.data
        roupa.categoria = form.categoria.data
        db.session.commit()
        flash('Roupa atualizada!', 'success')
        return redirect(url_for('produtos.listar_roupas'))
    return render_template('form_roupa.html', form=form, editar=True)

@produtos.route('/<int:id>/deletar', methods=['POST'])
def deletar_roupa(id):
    roupa = Roupa.query.get_or_404(id)
    db.session.delete(roupa)
    db.session.commit()
    flash('Roupa deletada com sucesso.', 'success')
    return redirect(url_for('produtos.listar_roupas'))
