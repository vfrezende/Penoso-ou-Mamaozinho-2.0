from backend.utils.utils import serialization_function
from flask import session, redirect, url_for
from functools import wraps


def serializable_class(cls: object) -> object:
    setattr(cls, "serialize", serialization_function)
    return cls


def is_logged_in(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if "logged_in" in session or True:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return wrap
