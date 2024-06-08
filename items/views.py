from django.shortcuts import render
from .models import Items
from rest_framework.views import APIView
from .serializer import ItemSerializer,BuyerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .tests  import Buyer
from rest_framework import status

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
    # Read or list items
    def get(self,request,id):
        list_of_items = Items.objects.filter(item_id=id)
        serializer_class = ItemSerializer(list_of_items,many=True)
        return Response (serializer_class.data)

    #Create an Item
    def post(self,request):
        serializer_obj = ItemSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            saved_item = serializer_obj.save()
            return Response("Success :" "Item '{}' created successfully".format(saved_item.name))
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)    

    # Update an item
    def put(self,request,id):
        item = Items.objects.get(item_id=id)
        serializer_obj = ItemSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            saved_item = serializer_obj.save()
            return Response(f'{"Success : ""Item '{}' updated succesfully".format(saved_item.name)}')