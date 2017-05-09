# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_purchaseditems_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodslist',
            name='subtotal',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='purchaseditems',
            name='subtotal',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
