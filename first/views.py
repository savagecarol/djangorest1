from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from rest_framework import status

@api_view(['GET','POST'])
def product_list(request):
    if request.method== 'GET':
        obj =Products.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)# Create your views here.

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT'])
def product_detail(request,pk):
    try:
        obj =Products.objects.get(id = pk)
    except Products.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' :
        serializer=ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer =ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)