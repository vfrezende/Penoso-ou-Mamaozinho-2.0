from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.model import models
from backend.config import CONFIG
from tests.e2e_tests.test_utils import User


class DatabaseHelper:

    def __init__(self):
        self.db = SQLAlchemy()
        self.models = models

        self._setup_db()

    def get_account(self,  username: str) -> Optional[models.Users]:
        return self.db.session.query(models.Users).filter_by(username=username).first()

    def create_account(self,  user: User) -> None:
        user_model = self.models.Users(
            name=user.name,
            email=user.email,
            username=user.username,
            password=user.password,
            picture=user.picture,
        )
        self.db.session.add(user_model)
        self.db.session.commit()

    def remove_account(self, username: str) -> None:
        account = self.get_account(username)
        if account:
            self.db.session.delete(account)
            self.db.session.commit()

    def clean_up(self) -> None:
        self.db.session.remove()
        self.db.session.expire_all()
        self.db.drop_all()

    def _setup_db(self):
        app = Flask(__name__)
        app.config.update(CONFIG)
        self.db.init_app(app)
        app.app_context().push()
