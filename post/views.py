from django.shortcuts import render
from .models import Goodslist
from  .models import PurchasedItems
from  django.http import JsonResponse
from django.http import  HttpResponse
# Create your views here.
def pos_list(request):
    return render(request, 'post/homepage.html', {'sum_count':PurchasedItems.shopping_cart()})
def shopping_list(request):
    posts = Goodslist.objects.all()
    if request.method== 'POST':
        purchase= PurchasedItems.objects.filter(goods_id=(request.POST['id']))
        if purchase :
            purchase[0].count = purchase[0].count + 1
            purchase[0].subtotal=purchase[0].price *purchase[0].count
            purchase[0].save()
        else:
            items = Goodslist.objects.filter(id=(request.POST['id']))
            new_purchase_item = {'count': 1,
                                 "classification":items[0].classification,
                                 "goods_id": items[0].id,
                                 "name": items[0].name,
                                 "price": items[0].price,
                                "unit": items[0].unit,
                                 "subtotal":items[0].price              }
            PurchasedItems.objects.create(**new_purchase_item)

        return HttpResponse(PurchasedItems.shopping_cart())

    return render(request, 'post/shopping_list.html', {'goodslist': posts,'sum_count':PurchasedItems.shopping_cart()})
def shopping_cart(request):
    carts=PurchasedItems.objects.all()
    if request.method == 'POST':
        goods= PurchasedItems.objects.filter(goods_id=(request.POST['id']))
        goods[0].count= goods[0].count+(int(request.POST['changecount']))
        print(request.POST['changecount'])
        goods[0].save()


    return render(request, 'post/shopping_cart.html', {'carts':carts,
                                                       'sum_count':PurchasedItems.shopping_cart()
                                                       })