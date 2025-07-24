from flask import Blueprint, render_template, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    usuario_id = session.get("usuario_id")
    usuario_tipo = session.get("usuario_tipo")
    return render_template('home.html', usuario_id=usuario_id, usuario_tipo=usuario_tipo)
