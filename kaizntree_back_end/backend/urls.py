from django.urls import path
from .views import ItemList, say_hello

urlpatterns = [
    path('', say_hello, name='say-hello'),
    path('dashboard/', ItemList.as_view(), name='item-list'),
    # Add more endpoints as needed
]
