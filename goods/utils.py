from django.db.models import Q
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    q = Q()
    for token in query.split():
        if len(token) > 2:
            q |= Q(name__icontains=token)
            q |= Q(description__icontains=token)

    return Products.objects.filter(q)