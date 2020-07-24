import pytest
from flask import url_for

from {{cookiecutter.app_slug}}.seeds import seeds_articles


@pytest.fixture(scope="class", autouse=True)
def seed():
    seeds_articles()


class TestArticleViews:

    def test_get_articles(self, client):
        resp = client.get(url_for('article.get_articles', article_id=1))
        articles_data = resp.get_json()['data']['articles']

        assert articles_data[0]['articleId'] == 1
        assert articles_data[1]['articleId'] == 2

    def test_get_article(self, client):
        resp = client.get(url_for('article.get_article', article_id=1))
        article_data = resp.get_json()['data']['article']

        assert article_data['articleId'] == 1

    def test_get_article_not_exited(self, client):
        resp = client.get(url_for('article.get_article', article_id=999))
        error_data = resp.get_json()['error']

        assert error_data["code"] == 404

    def test_get_article_by_title(self, client):
        resp = client.get(url_for('article.get_article_by_title', title='a1'))
        article_data = resp.get_json()['data']['article']

        assert article_data['articleId'] == 1

    def test_get_article_not_existed_by_title(self, client):
        resp = client.get(url_for('article.get_article_by_title', title='xxx'))
        error_data = resp.get_json()['error']

        assert error_data["code"] == 404

    def test_post_articles(self, client):
        json_data = {
            "title": "test title",
            "description": "test decription",
            "body": "test body",
        }
        resp = client.post(url_for('article.post_articles'), json=json_data)
        article_data = resp.get_json()['data']['article']

        assert article_data['articleId'] == 3
        assert article_data['tags'] == []
        assert article_data['createdAt'] != ""

    def test_post_articles_with_wrong_data(self, client):
        json_data = {
            "title": "test title 2",
            "description": "test decription 2",
            "bodyyy": "updated body",
        }
        resp = client.post(url_for('article.post_articles'), json=json_data)
        error_data = resp.get_json()['error']

        assert error_data['code'] == 400

    def test_put_article(self, client):
        json_data = {
            "title": "updated title",
            "description": "updated decription",
            "body": "updated body",
        }
        resp = client.put(
            url_for('article.put_article', article_id=1), json=json_data)
        article_data = resp.get_json()['data']['article']

        assert article_data["articleId"] == 1
        assert 'updated' in article_data["title"]
        assert 'updated' in article_data["description"]
        assert 'updated' in article_data["body"]

    def test_put_article_not_existed(self, client):
        json_data = {
            "title": "updated title",
            "description": "updated decription",
            "body": "updated body",
        }
        resp = client.put(url_for('article.put_article',
                                  article_id=999), json=json_data)
        error_data = resp.get_json()['error']

        assert error_data["code"] == 404

    def test_put_article_with_wrong_data(self, client):
        json_data = {
            "title": "updated title",
            "description": "updated decription",
            "bodyyy": "updated body",
        }
        resp = client.put(
            url_for('article.put_article', article_id=1), json=json_data)
        error_data = resp.get_json()['error']

        assert error_data['code'] == 400

    def test_delete_article(self, client):
        resp = client.delete(url_for('article.delete_article', article_id=1))
        assert resp.status_code == 204

    def test_delete_article_not_existed(self, client):
        resp = client.delete(url_for('article.delete_article', article_id=999))
        assert resp.status_code == 204

    def test_get_categories(self, client):
        resp = client.get(url_for('article.get_categories'))
        categories_data = resp.get_json()['data']['categories']

        assert len(categories_data) == 2
        assert categories_data[0]['name'] == "c1"
        assert categories_data[0]['tags'][0]['tagId'] == 1
        assert categories_data[1]['name'] == "c2"
        assert categories_data[1]['tags'][0]['tagId'] == 2

    def test_get_tags(self, client):
        resp = client.get(url_for('article.get_tags'))
        tags_data = resp.get_json()['data']['tags']

        assert len(tags_data) == 2
        assert tags_data[0]['tagId'] == 1
        assert tags_data[1]['tagId'] == 2
