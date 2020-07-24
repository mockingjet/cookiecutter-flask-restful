import os
import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .settings import Config

{%- if cookiecutter.database == "sqlite" %}
engine = create_engine(Config.DATABASE_URI)
{%- elif cookiecutter.database == "postgres" %}
engine = create_engine(
    Config.DATABASE_URI,
    pool_size=2,
    max_overflow=1,
    pool_timeout=2,
    pool_recycle=3600,
    pool_pre_ping=True)
{%- endif %}


# singleton
db_session = scoped_session(sessionmaker(engine))
# sa basic model
Base = declarative_base()


class Model(Base):
    __abstract__ = True
    query = db_session.query_property()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def save(self):
        db_session.add(self)
        db_session.commit()
        return self

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class SaAutoCamelSchema(SQLAlchemyAutoSchema):
    """For marshmallow schemas that use camelCase for its external representation
    and snake_case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)
