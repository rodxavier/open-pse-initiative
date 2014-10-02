# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_is_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_currently_listed',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='is_suspended',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='listing_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
