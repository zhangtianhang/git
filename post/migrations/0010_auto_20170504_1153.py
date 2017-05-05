# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20170504_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodslist',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='purchaseditems',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
