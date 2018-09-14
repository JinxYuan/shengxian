# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shengxianapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sxuser',
            name='uaddress',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='sxuser',
            name='uphone',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='sxuser',
            name='ushouname',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='sxuser',
            name='uyoubian',
            field=models.CharField(max_length=6, default=''),
        ),
    ]
