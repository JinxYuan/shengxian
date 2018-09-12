# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SXUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ushouname', models.CharField(max_length=10)),
                ('uaddress', models.CharField(max_length=100)),
                ('uyoubian', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
