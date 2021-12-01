from rest_framework import generics
from .models import Item

from .serializers import ItemSerializer


class ItemList(generics.ListAPIView):
    """
    Provides a get method handler to list all the items.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveAPIView):
    """
    Provides a get method handler to retrieve a single item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
