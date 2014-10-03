# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_company_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=tinymce.models.HTMLField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='renamed_to',
            field=models.ForeignKey(related_name=b'renamed_from', default=None, blank=True, to='companies.Company', null=True),
            preserve_default=True,
        ),
    ]
