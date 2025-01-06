from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

# List and Create
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update, and Delete
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
   
def index(request):
     return render(request, 'api/index.html')
