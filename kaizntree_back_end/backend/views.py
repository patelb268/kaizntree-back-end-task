from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Item, Category, Tag, TagItem
from .forms import ItemForm, CategoryForm
from .serializers import ItemSerializer, CategorySerializer, TagSerializer

# Create your views here.
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def say_hello(request):  # Accept the request parameter
    return HttpResponse('Hello world')  # Use HttpResponse instead of HTTPResponse

def register(request):
    """
    Register a new user.
    Method:
        - POST
    Request Body:
        - Form data for user registration. See UserCreationForm for the expected format.
    Response:
        - Status Code: 302 Found (redirects to /dashboard/ on successful registration)
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    """
    Log in a user.
    Method:
        - POST
    Request Body:
        - Form data for user login. See AuthenticationForm for the expected format.
    Response:
        - Status Code: 302 Found (redirects to /dashboard/ on successful login)
    """

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    """
    Log out the user.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 302 Found (redirects to /login/ on successful logout)
    """

    logout(request)
    return redirect('/')
