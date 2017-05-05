# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170504_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('goods_id', models.IntegerField(default=0)),
                ('classification', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=10)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('unit', models.CharField(default='', max_length=10)),
                ('subtotal', models.FloatField(default=0, max_length=10)),
            ],
        ),
    ]
