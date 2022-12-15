from rest_framework import generics
import io, csv, pandas as pd
from django.shortcuts import render
from django.core.files.base import ContentFile
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer,FileUploadSerializer
from rest_framework.decorators import api_view

        # Read All Item
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
       
        return queryset

        # Create
@api_view(['POST'])
def itemCreate(request):
	serializer = ItemSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

      # Update
@api_view(['POST'])
def itemUpdate(request, pk):
	task = Item.objects.get(id=pk)
	serializer = ItemSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

    # Delete
@api_view(['DELETE'])
def itemDelete(request, pk):
	task = Item.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

     # Specific Read a Item
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



       # Upload any CSV in anytime

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Item(
                       trade_code = row['trade_code'],
                       date= row["date"],
                       open= row['open'],
                       close= row["close"],
                       high= row["high"],
                       low= row["low"],
                       volume= row["volume"],
                       )
            new_file.save()
        return Response("file uploaded")