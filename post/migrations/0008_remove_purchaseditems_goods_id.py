# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_purchaseditems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditems',
            name='goods_id',
        ),
    ]
