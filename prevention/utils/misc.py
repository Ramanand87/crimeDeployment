import yaml
from django.conf import settings


def yaml_coerce(value):
    if isinstance(value, str):
        return yaml.load("dummy: " + value, Loader=yaml.SafeLoader)["dummy"]

    return value


import os


def get_secret_key():
    return settings.SECRET_KEY


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_env_variable(var_name, default=None):
    return os.environ.get(var_name, default)


# def hex_to_bytes(hex_string: str) -> bytes:
#     return bytes.fromhex(hex_string)


# def bytes_to_hex(bytes_: bytes) -> str:
#     return bytes(bytes_).hex()


# def apply_on_commit(callable_):
#     if settings.USE_ON_COMMIT_HOOK:
#         transaction.on_commit(callable_)
#     else:
#         callable_()
