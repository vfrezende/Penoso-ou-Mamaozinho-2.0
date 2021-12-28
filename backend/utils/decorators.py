from backend.utils.utils import serialization_function


def serializable_class(cls: object) -> object:
    setattr(cls, "serialize", serialization_function)
    return cls
