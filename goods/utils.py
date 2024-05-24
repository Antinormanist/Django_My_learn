from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchRank


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")