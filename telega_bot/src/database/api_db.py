from peewee import CharField
from ..config_data.consts import DATABASE_PATH, FINDED_API_DB
from .base_model import base_model


@base_model(DATABASE_PATH + FINDED_API_DB)
class Api:
    url = CharField()
    name = CharField()
    annotation = CharField()
    auth = CharField()
