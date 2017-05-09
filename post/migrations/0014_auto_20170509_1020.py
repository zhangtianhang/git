# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20170509_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodslist',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='purchaseditems',
            name='subtotal',
        ),
    ]
