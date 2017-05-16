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
        if goods:
            print(request.POST['changecount'])
            count = int(request.POST['changecount'])
            goods[0].count = goods[0].count + count
            goods[0].subtotal = goods[0].price * goods[0].count
            if goods[0].count==0:
                goods.delete()
                goods.save()
            goods[0].save()
        sub_count=goods[0].count
        subtotal=goods[0].subtotal
        result={'sub_count':sub_count,'subtotal':subtotal}

        return JsonResponse(result)
    return render(request, 'post/shopping_cart.html', {'carts':carts,
                                                       'sum_count':PurchasedItems.shopping_cart()
                                                       })