# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170421_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodslist',
            old_name='分类',
            new_name='classification',
        ),
        migrations.RenameField(
            model_name='goodslist',
            old_name='名称',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='goodslist',
            old_name='单价',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='goodslist',
            old_name='单位',
            new_name='unit',
        ),
    ]
