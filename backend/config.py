import os
from dotenv import load_dotenv


load_dotenv()


def getConfig():
    conf = {}

    conf["SECRET_KEY"] = os.getenv("SECRET_KEY")
    conf["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_CONNECTION_URI")
    conf["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    return conf


CONFIG = getConfig()
