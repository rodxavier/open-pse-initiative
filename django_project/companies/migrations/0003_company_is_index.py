# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20140909_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_index',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
