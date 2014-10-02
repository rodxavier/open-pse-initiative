# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20141001_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='listing_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
