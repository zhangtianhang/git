# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_preferential'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferential',
            name='goods_id',
            field=models.IntegerField(default=1),
        ),
    ]
