# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20170510_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditems',
            name='subtotal',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
