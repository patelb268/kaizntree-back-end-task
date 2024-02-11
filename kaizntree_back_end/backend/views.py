from django.http import HttpResponse  # Correct import
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def say_hello(request):  # Accept the request parameter
    return HttpResponse('Hello world')  # Use HttpResponse instead of HTTPResponse