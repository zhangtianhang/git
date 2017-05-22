from django.shortcuts import render
from .models import Goodslist
from  .models import PurchasedItems
from  .models import Preferential
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

    total=0
    carts=PurchasedItems.objects.all()
    for goods in carts:
        if Preferential.objects.filter(goods_id=goods.goods_id):
            goods.subtotal =goods.price * (goods.count - int(goods.count / 3))
            goods.freecount = int(goods.count / 3)
        else:
            goods.subtotal = goods.price * goods.count
        goods.costprice = goods.price * goods.count
        goods.save()
        total+=goods.subtotal
    PurchasedItems.objects.filter(count=0).delete()
    if request.method == 'POST':
        goods= PurchasedItems.objects.filter(goods_id=(request.POST['id']))
        if goods:
            count = int(request.POST['changecount'])
            goods[0].count = goods[0].count + count
            preferential=Preferential.objects.filter(goods_id=(request.POST['id']))
            if Preferential.objects.filter(goods_id=(request.POST['id'])):
                goods[0].subtotal=preferential[0].price * (goods[0].count - int(goods[0].count / 3))
                goods[0].freecount = int(goods[0].count / 3)
                goods[0].save()
               

            else:
                goods[0].subtotal = goods[0].price * goods[0].count
            goods[0].costprice= goods[0].price * goods[0].count
            if goods[0].count==0:
                goods[0].delete()
                sub_count=0

            else:
                goods[0].save()
                sub_count=goods[0].count
        subtotal=goods[0].subtotal
        costprice=goods[0].costprice
        sum_count=PurchasedItems.shopping_cart()
        total = PurchasedItems.shopping_total()
        result={'sub_count':sub_count,'subtotal':subtotal,'sum_count':sum_count,'costprice':costprice,'total':total}

        return JsonResponse(result)

    return render(request, 'post/shopping_cart.html', {'carts':carts,
                                                       'sum_count':PurchasedItems.shopping_cart(),
                                                       'total':total,

                                                       })
def go(request):

    carts = PurchasedItems.objects.all()

    preferrntial_goods = carts.exclude(freecount=0)
    if request.method == 'POST':
        PurchasedItems.objects.all().delete()
        return HttpResponse()
    total = 0
    save = 0
    for goods in PurchasedItems.objects.all():
        total += goods.subtotal
        save += goods.costprice
    save = save - total

    return render(request, 'post/go.html',{
                                           'carts':carts,
                                           'sum_count':PurchasedItems.shopping_cart(),
                                           'total':total,
                                           'save':save,
                                           'preferrntial_goods':preferrntial_goods

                                           })
