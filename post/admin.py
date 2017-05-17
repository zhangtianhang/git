
from django.contrib import admin
from .models import  Goodslist
from .models import PurchasedItems
from .models import Preferential

admin.site.register(Goodslist)
admin.site.register(PurchasedItems)
admin.site.register(Preferential)