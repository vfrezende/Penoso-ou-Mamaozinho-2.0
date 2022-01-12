from flask.blueprints import Blueprint
from backend.routes import VIEWS_BASE_NAME
from backend.routes.views.home import home_blueprint
from backend.routes.views.disciplinas import disciplinas_blueprint
from backend.routes.views.usuarios import usuarios_blueprint


views_blueprint = Blueprint(VIEWS_BASE_NAME, __name__)

views_blueprint.register_blueprint(home_blueprint)
views_blueprint.register_blueprint(disciplinas_blueprint)
views_blueprint.register_blueprint(usuarios_blueprint)
