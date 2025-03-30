from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Optional: Register error handlers
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Initialize extensions here (e.g., database, migrations, login_manager, etc.)
    
    return app
