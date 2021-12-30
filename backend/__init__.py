from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from backend.config import CONFIG
from backend.utils.encoders import PoMEncoder


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/templates/static",
)

app.json_encoder = PoMEncoder
app.config.update(CONFIG)

db = SQLAlchemy(app)
CORS(app)

# must import after create app
from backend import routes
