# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20170516_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditems',
            name='costprice',
            field=models.FloatField(max_length=10, default=0),
        ),
    ]
