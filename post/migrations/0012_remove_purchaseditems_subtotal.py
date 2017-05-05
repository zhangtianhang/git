# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20170504_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditems',
            name='subtotal',
        ),
    ]
