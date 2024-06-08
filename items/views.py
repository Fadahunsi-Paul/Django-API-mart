from django.shortcuts import render
from .models import Items
from rest_framework.views import APIView
from .serializer import ItemSerializer,BuyerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .tests  import Buyer

@api_view(['GET','POST']) 
@permission_classes([IsAuthenticated])
def list_of_items(request):
    all_items = Items.objects.all()
    serializer_class = ItemSerializer(all_items,many=True)

    context = {
        'serializer_class_data':serializer_class.data
    }
    return Response(serializer_class.data)

@api_view(['GET','POST'])
def buyer_view(request):
    buyer_obj = Buyer('Dafa','hunsi@gmail.com') 
    serializer_class = BuyerSerializer(buyer_obj,many=False)
    return Response (serializer_class.data)


#Class Based ApiView
class ItemsList(APIView):

    def get(self,request):
        list_of_items = Items.objects.all()
        serializer_class = ItemSerializer(list_of_items,many=True)
        return Response (serializer_class.data)

class ItemListDetails(APIView):
    def get(self,request,id):
        list_of_items = Items.objects.filter(item_id=id)
        serializer_class = ItemSerializer(list_of_items,many=True)
        return Response (serializer_class.data)