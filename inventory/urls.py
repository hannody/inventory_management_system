from django.urls import path
from .views import (ItemList, ItemDetail, ItemListRender, ItemDetailTemplateRendering)

urlpatterns = [
    path('api/inventory/', ItemList.as_view()),
    path('inventory/', ItemListRender.as_view()),
    path('inventory/<uuid:pk>/', ItemDetail.as_view()),
    path('inventory/html/<uuid:pk>/', ItemDetailTemplateRendering.as_view()),
]
