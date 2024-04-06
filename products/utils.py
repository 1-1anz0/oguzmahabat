from django.contrib.postgres.search import SearchVector, SearchQuery
from products.models import Products


def search(query, cat_search):
    if cat_search and query:
        return Products.objects.annotate(search=SearchVector('title', 'description')).filter(category__id=cat_search, search=SearchQuery(query))

    elif cat_search == '4':
        return Products.objects.all()
    elif cat_search:
        return Products.objects.filter(category__id=cat_search)