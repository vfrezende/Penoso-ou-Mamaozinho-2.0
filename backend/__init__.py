from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from backend.config import CONFIG


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/templates/static",
)

app.config.update(CONFIG)

db = SQLAlchemy(app)
CORS(app)

# must import after create app
from backend import routes
