# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_date', models.DateField()),
                ('price_open', models.DecimalField(max_digits=20, decimal_places=10)),
                ('price_high', models.DecimalField(max_digits=20, decimal_places=10)),
                ('price_low', models.DecimalField(max_digits=20, decimal_places=10)),
                ('price_close', models.DecimalField(max_digits=20, decimal_places=10)),
                ('volume', models.BigIntegerField(null=True, blank=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
            options={
                'ordering': ('quote_date', 'company'),
            },
            bases=(models.Model,),
        ),
    ]
