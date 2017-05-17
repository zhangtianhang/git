# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_purchaseditems_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferential',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('classification', models.CharField(null='', max_length=10)),
                ('name', models.CharField(null='', max_length=10)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('unit', models.CharField(default='', max_length=10)),
                ('count', models.IntegerField(default=1)),
                ('subtotal', models.FloatField(default=0, max_length=10)),
            ],
        ),
    ]
