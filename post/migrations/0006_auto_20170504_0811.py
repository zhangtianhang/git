# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170424_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodslist',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='price',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='unit',
            field=models.CharField(max_length=10),
        ),
    ]
