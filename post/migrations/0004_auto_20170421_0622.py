# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170421_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodslist',
            name='单价',
            field=models.DecimalField(max_digits=15, decimal_places=1),
        ),
    ]
