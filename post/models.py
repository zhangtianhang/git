from django.db import  models
from django.utils import timezone
class Goodslist(models.Model):
    author = models.ForeignKey('auth.User')
    classification=models.CharField(max_length=10,default='')
    name= models.CharField(max_length=10,default='')
    price=models.FloatField(max_length=10,default=0)
    unit=models.CharField(max_length=10,default='')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

        def __str__(self):
            return self.classification
class PurchasedItems(models.Model):
    count=models.IntegerField(default=0,null=False)
    goods_id=models.IntegerField(default=1,null=False)
    classification=models.CharField(max_length=10,default='')
    name= models.CharField(max_length=10,default='')
    price=models.FloatField(max_length=10,default=0)
    unit=models.CharField(max_length=10,default='')
    subtotal= models.FloatField(max_length=10, default=0)
    costprice=models.FloatField(max_length=10, default=0)

    freecount = models.IntegerField(default=1,null=False)

    def __str__(self):
        return self.classification
    @classmethod
    def shopping_cart(cls):
        sum_count = 0
        for count  in PurchasedItems.objects.all():
            sum_count = sum_count + count.count
        return sum_count
class Preferential(models.Model):
    classification = models.CharField(max_length=10, null='')
    name = models.CharField(max_length=10, null='')
    price = models.FloatField(max_length=10,default=0)
    unit =models.CharField(max_length=10,default='')
    count = models.IntegerField(default=1,null=False)
    goods_id = models.IntegerField(default=1, null=False)
    subtotal = models.FloatField(max_length=10, default=0)

    def __str__(self):
        return self.classification
