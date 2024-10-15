from flask import Flask
from .models import db  # Import db here
from .routes import blog

def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)  # Initialize db with the app

    # Register the blog blueprint
    app.register_blueprint(blog)

    return app
