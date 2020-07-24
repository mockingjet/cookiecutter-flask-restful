import sys
sys.dont_write_bytecode = True

import pytest

from {{cookiecutter.app_slug}}.app import create_app
from {{cookiecutter.app_slug}}.settings import TestConfig
from {{cookiecutter.app_slug}}.database import engine, db_session, Base


@pytest.fixture(scope="module")
def app():
    app = create_app(TestConfig)
    ctx = app.test_request_context()
    ctx.push()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield app

    db_session.remove()
    Base.metadata.drop_all(engine)
    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()
