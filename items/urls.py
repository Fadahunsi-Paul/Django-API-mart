from django.urls import path,include
from .import views
from items.views import ItemsList,ItemListDetails

urlpatterns = [
    path('item_list/',views.list_of_items,name='item_list'),
    path('buyer_list/',views.buyer_view,name='buyer_list'),
    path('itemList/',ItemsList.as_view(),name='itemlist'),
    path('item_detail/<int:id>/',ItemListDetails.as_view(),name='item_detail'),
    path('itemMixin/',views.ItemListMixins.as_view(),name= 'item_mixin'),
]
