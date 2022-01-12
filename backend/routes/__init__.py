BLUEPRINT_NAME_TEMPLATE = "{}-{}"
API_BASE_NAME = "api"
VIEWS_BASE_NAME = "views"


def get_blueprint_name(module_name, blueprint_name):
    return BLUEPRINT_NAME_TEMPLATE.format(module_name, blueprint_name)
