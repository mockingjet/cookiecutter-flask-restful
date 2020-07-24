from {{cookiecutter.app_slug}}.modules.article.models import Article, Category, Tag


def seeds_articles():
    """
    seeds 2 categories => c1, c2

    seeds 2 tags => t1 belongs to c1, t2 belongs to c2

    seeds 2 articles => a1 has t1, a2 has t2
    """
    c1 = Category('c1').save()
    c2 = Category('c2') .save()

    t1 = Tag('t1', c1) .save()
    t2 = Tag('t2', c2) .save()

    a1 = Article(title="a1",
                 description="a1 description",
                 body="a1 body")
    a1.tags.append(t1)
    a1.save()
    a2 = Article(title="a2",
                 description="a2 description",
                 body="a2 body")
    a2.tags.append(t2)
    a2.save()
