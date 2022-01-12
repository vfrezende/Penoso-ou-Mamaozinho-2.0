from flask import Flask
from flask_cors import CORS

from backend.model import db
from backend.config import CONFIG
from backend.utils.encoders import PoMEncoder


def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/templates/static",
    )

    app.json_encoder = PoMEncoder
    app.config.update(CONFIG)

    CORS(app)

    db.init_app(app)

    with app.app_context():

        from backend.routes.api import api_blueprint

        app.register_blueprint(api_blueprint)

        from backend.routes.views import views_blueprint

        app.register_blueprint(views_blueprint)

    return app
