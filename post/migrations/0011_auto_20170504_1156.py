# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20170504_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditems',
            name='goods_id',
            field=models.IntegerField(default=1),
        ),
    ]
