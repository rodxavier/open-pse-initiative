# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ('-quote_date', 'company')},
        ),
        migrations.AlterUniqueTogether(
            name='quote',
            unique_together=set([('company', 'quote_date')]),
        ),
    ]
