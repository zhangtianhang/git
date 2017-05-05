# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_remove_purchaseditems_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditems',
            name='goods_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='classification',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='name',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='price',
            field=models.FloatField(max_length=10, default=0),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='unit',
            field=models.CharField(max_length=10, default=''),
        ),
    ]
