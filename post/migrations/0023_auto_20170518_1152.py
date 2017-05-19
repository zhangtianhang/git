# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_purchaseditems_costprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditems',
            name='freecount',
            field=models.IntegerField(default=0),
        ),
    ]
