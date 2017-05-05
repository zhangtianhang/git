# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170421_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodslist',
            name='单价',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
