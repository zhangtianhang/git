# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_purchaseditems_freecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditems',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
