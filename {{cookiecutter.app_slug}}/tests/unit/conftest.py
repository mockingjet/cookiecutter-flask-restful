import sys
sys.dont_write_bytecode = True

import pytest

from {{cookiecutter.app_slug}}.modules.article.models import Article, Tag, Category


@pytest.fixture()
def article():
    yield Article(title="cats are cute",
                  description="cats are so cute",
                  body="cats are sooooo cute")


@pytest.fixture()
def category():
    yield Category("animal")


@pytest.fixture()
def tag(category):
    yield Tag(name="cat", category=category)
