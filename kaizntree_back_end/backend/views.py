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

@login_required
def dashboard(request):
    """
    Get the user's dashboard.
    Method:
        - GET
    Authentication:
        - Login required
    Response:
        - Status Code: 200 OK
        - Body: HTML content for the dashboard.
    """

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        in_stock_min = request.POST.get('in_stock_min')
        in_stock_max = request.POST.get('in_stock_max')
        available_stock_min = request.POST.get('available_stock_min')
        available_stock_max = request.POST.get('available_stock_max')
        search = request.POST.get('search')
        print(category_id, in_stock_min, in_stock_max, available_stock_min, available_stock_max, search)

        filters = {}
        if category_id:
            filters['category__id'] = category_id
        if in_stock_min:
            filters['in_stock__gte'] = in_stock_min
        if in_stock_max:
            filters['in_stock__lte'] = in_stock_max
        if available_stock_min:
            filters['available_stock__gte'] = available_stock_min
        if available_stock_max:
            filters['available_stock__lte'] = available_stock_max
        if search:
            filters['name__icontains'] = search

        items = Item.objects.filter(**filters)
    else:
        items = Item.objects.all()

    categories = Category.objects.all()
    tags = Tag.objects.all()
    tag_item = TagItem.objects.all()
    new_items = []
    for item in items:
        tags = tag_item.filter(sku=item.id)
        item.tags = tags
        new_items.append(item)

    return render(request, 'dashboard.html', {'categories': categories, 'tags': tags, 'items': new_items})

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
