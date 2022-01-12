from flask.blueprints import Blueprint

from backend.routes import API_BASE_NAME
from backend.routes.api.arquivos import api_arquivos_blueprint
from backend.routes.api.comentarios import api_comentarios_blueprint
from backend.routes.api.disiciplinas import api_disciplinas_blueprint
from backend.routes.api.links import api_links_blueprint
from backend.routes.api.usuarios import api_usuarios_blueprint


api_blueprint = Blueprint(API_BASE_NAME, __name__)

api_blueprint.register_blueprint(api_arquivos_blueprint)
api_blueprint.register_blueprint(api_comentarios_blueprint)
api_blueprint.register_blueprint(api_disciplinas_blueprint)
api_blueprint.register_blueprint(api_links_blueprint)
api_blueprint.register_blueprint(api_usuarios_blueprint)
