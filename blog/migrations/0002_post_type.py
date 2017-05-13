# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(max_length=20, default='freeboard', choices=[('notice', 'notice'), ('freeboard', 'freeboard')]),
        ),
    ]
