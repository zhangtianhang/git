# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20170509_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodslist',
            name='subtotal',
            field=models.FloatField(max_length=10, default=0),
        ),
    ]
