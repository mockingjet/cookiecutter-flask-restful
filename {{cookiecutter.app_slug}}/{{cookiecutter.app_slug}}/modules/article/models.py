import datetime as dt

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, TEXT, Table, ForeignKey

from {{cookiecutter.app_slug}}.database import Model

articles_assoc_tags = Table(
    "articles_assoc_tags", Model.metadata,
    Column("tag_id", Integer, ForeignKey('tags.tag_id')),
    Column("article_id", Integer, ForeignKey('articles.article_id')))


class Category(Model):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    tags = relationship("Tag", back_populates="category")

    def __init__(self, name):
        Model.__init__(self, name=name)


class Tag(Model):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    category = relationship("Category", back_populates="tags")
    articles = relationship("Article", secondary=articles_assoc_tags,
                            back_populates="tags")

    def __init__(self, name, category):
        Model.__init__(self, name=name, category=category)


class Article(Model):
    __tablename__ = "articles"

    article_id = Column(Integer, primary_key=True)
    title = Column(String(30), unique=True, index=True)
    description = Column(String(120))
    body = Column(TEXT)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    tags = relationship("Tag", secondary=articles_assoc_tags,
                        back_populates="articles")

    def __init__(self, title, description, body, **kwargs):
        Model.__init__(self, title=title,
                       description=description, body=body, **kwargs)

    def add_tag(self, tag: Tag):
        self.tags.append(tag)

    def remove_tag(self, tag: Tag):
        if tag in self.tags:
            self.tags.remove(tag)
