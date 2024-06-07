from django.urls import path,include
from .import views

urlpatterns = [
    path('item_list/',views.list_of_items,name='item_list'),
    path('buyer_list/',views.buyer_view,name='buyer_list'),
]
