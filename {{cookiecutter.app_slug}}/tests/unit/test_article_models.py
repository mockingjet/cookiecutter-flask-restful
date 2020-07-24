import pytest


class TestArticleModels:

    def test_article_add_tag(self, article, tag):
        article.add_tag(tag)

        assert tag in article.tags
        assert article in tag.articles

    def test_article_remove_tag(self, article, tag):
        article.add_tag(tag)
        article.remove_tag(tag)

        assert tag not in article.tags

    def test_article_remove_tag_not_included(self, article, tag):
        article.remove_tag(tag)

        assert tag not in article.tags
