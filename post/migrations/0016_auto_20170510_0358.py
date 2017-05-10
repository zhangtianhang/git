# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_goodslist_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodslist',
            name='count',
        ),
        migrations.RemoveField(
            model_name='goodslist',
            name='subtotal',
        ),
    ]
