from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

"""Create the database and initialize the Flask app with necessary configurations."""
def create_db(app):
    with app.app_context():
        db.create_all()
        create_admin()
        print("✅Database created successfully.")


"""Create an admin user if it doesn't exist."""
def create_admin(emailField=None, passwordField=None):
    from app.models.usuario import Usuario

    # Check if an admin user already exists
    existing_admin = Usuario.query.filter_by(tipo='admin').first()
    if existing_admin:
        print("⚠️Admin user already exists.")
        return
    
    user = Usuario(
        nome="Admin",
        email=emailField or "admin@gmail.com",
        tipo="admin",
    )
    user.set_senha(passwordField or "adm123")  # Set a default password
    db.session.add(user)
    db.session.commit()
    print("✅Admin user created successfully.")


"""Create and configure the Flask application."""
def create_app():
    app = Flask(__name__)

    csrf = CSRFProtect(app)
    
    # Load environment variables
    load_dotenv()

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///banco.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Register blueprints or routes here if needed
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    from app.routes.produto import produtos
    app.register_blueprint(produtos)
    from app.routes.auth_context import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.usuario import usuarios_bp
    app.register_blueprint(usuarios_bp)

    return app