from backend.utils.utils import serialization_function
import flask
from functools import wraps


def serializable_class(cls: object) -> object:
    setattr(cls, "serialize", serialization_function)
    return cls


def is_logged_in(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if flask.session.get("logged_in"):
            return func(*args, **kwargs)
        else:
            return flask.redirect(flask.url_for("views.views-usuarios.login"))
    return wrap
