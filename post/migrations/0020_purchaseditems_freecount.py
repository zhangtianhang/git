# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_preferential_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditems',
            name='freecount',
            field=models.IntegerField(default=1),
        ),
    ]
