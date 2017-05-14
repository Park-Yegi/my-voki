# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170513_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
