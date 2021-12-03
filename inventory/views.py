from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Item

from .serializers import ItemSerializer


class ItemList(generics.ListAPIView):
    """
    Provides a get method handler to list all the items.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListRender(generics.ListAPIView):
    """
    Provides a get method handler to list all the items.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory_list.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'items': queryset})


# class ItemDetail(generics.RetrieveAPIView):
#     """
#     Provides a get method handler to retrieve a single item.
#     """
#     queryset = Item.objects.all()
#     #serializer_class = ItemSerializer
#     renderer_classes = (TemplateHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'item': self.object}, template_name='item_detail.html')

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
