# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20141001_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='order',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
