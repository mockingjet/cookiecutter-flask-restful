from flask import Blueprint, request
from marshmallow import ValidationError

from {{cookiecutter.app_slug}}.utils import wrap_response
from {{cookiecutter.app_slug}}.exceptions import APIError
from .models import Article, Tag, Category
from .schemas import ArticleSchema, TagSchema, CategorySchema


bp = Blueprint('article', __name__)


@bp.route('/articles')
@wrap_response()
def get_articles():
    articles = Article.query.all()
    articles_schema = ArticleSchema(many=True)

    return {"articles": articles_schema.dump(articles)}


@bp.route('/articles', methods=['POST'])
@wrap_response()
def post_articles():
    json_data = request.get_json()
    article_schema = ArticleSchema()

    try:
        data = article_schema.load(json_data)
    except ValidationError as verr:
        raise APIError(400, "invalid input", input_error=verr.messages)

    try:
        article = Article.create(**data)
    except Exception as err:
        raise APIError(message=str(err))

    return {"article": article_schema.dump(article)}


@bp.route('/articles/<int:article_id>')
@wrap_response()
def get_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        raise APIError(404, ["article not found"])

    article_schema = ArticleSchema()
    return {"article": article_schema.dump(article)}


@bp.route('/articles/<title>')
@wrap_response()
def get_article_by_title(title):
    article = Article.query.filter(Article.title == title).first()
    if not article:
        raise APIError(404, "article not found")

    article_schema = ArticleSchema(exclude=['tags.category'])
    return {"article": article_schema.dump(article)}


@bp.route('/articles/<int:article_id>', methods=['PUT'])
@wrap_response()
def put_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        raise APIError(404, "article not found")

    json_data = request.get_json()
    article_schema = ArticleSchema(exclude=['tags.category'])

    try:
        data = article_schema.load(json_data)
    except ValidationError as verr:
        raise APIError(400, "invalid input", input_error=verr.messages)

    try:
        article.update(**data)
    except Exception as err:
        raise APIError(message=str(err))

    return {"article": article_schema.dump(article)}


@bp.route('/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return {}, 204

    try:
        article.delete()
    except Exception as err:
        raise APIError(message=str(err))

    return {}, 204


@bp.route('/categories')
@wrap_response()
def get_categories():
    categories = Category.query.all()

    categories_schema = CategorySchema(many=True)
    return {"categories": categories_schema.dump(categories)}


@bp.route('/tags')
@wrap_response()
def get_tags():
    tags = Tag.query.all()

    tags_schema = TagSchema(many=True)
    return {"tags": tags_schema.dump(tags)}
