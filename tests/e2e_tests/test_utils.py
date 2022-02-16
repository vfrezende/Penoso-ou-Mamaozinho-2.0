from dataclasses import dataclass
from enum import Enum
import random
import string


class Paths(str, Enum):
    HOME_PATH = '/home'
    LOGIN_PATH = '/login'
    REGISTER_PATH = '/register'


@dataclass
class User:
    name: str
    email: str
    username: str
    password: str
    picture: str


def build_random_string_with_prefix(prefix: str, length: int = 5) -> str:
    return prefix + '_' + ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def build_random_string_with_suffix(suffix: str, length: int = 5) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length)) + '_' + suffix
