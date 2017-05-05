
from django.contrib import admin
from .models import  Goodslist
from .models import PurchasedItems

admin.site.register(Goodslist)
admin.site.register(PurchasedItems)