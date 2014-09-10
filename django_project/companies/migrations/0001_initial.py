# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, null=True, blank=True)),
                ('symbol', models.CharField(max_length=10, blank=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('symbol',),
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model,),
        ),
    ]
