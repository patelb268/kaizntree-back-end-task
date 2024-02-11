from django.contrib import admin
from .models import Item, Tag
from .models import Category
from .models import User
# Register your models here.
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)
