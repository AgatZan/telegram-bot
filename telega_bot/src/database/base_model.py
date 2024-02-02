from peewee import Model, SqliteDatabase
from functools import update_wrapper


def base_model(db_path: str):
    def cls_creator(cls) -> Model:
        db = SqliteDatabase(db_path)

        class BaseModel(Model):
            class Meta:
                database = db

        return type(
            cls.__name__,
            (BaseModel, *cls.mro()),
            {
                **cls.__dict__,
                **BaseModel.__dict__,
            },
        )

    return cls_creator
