# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonTradingDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('non_trading_date', models.DateField()),
            ],
            options={
                'ordering': ('non_trading_date',),
                'verbose_name': 'Non Trading Day',
                'verbose_name_plural': 'Non Trading Days',
            },
            bases=(models.Model,),
        ),
    ]
