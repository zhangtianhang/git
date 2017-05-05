from django import forms
from  .models import Purchasedgoods
class PurchasedgoodsForm(forms.ModelForm):
    class Meta:
        model=Purchasedgoods
        fields=('classification','name','unit',' price',)