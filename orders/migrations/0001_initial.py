# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'ABC', unique=True, max_length=200)),
                ('status', models.CharField(default=b'Started', max_length=200, choices=[(b'Started', b'Started'), (b'Processing', b'Processing'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')])),
                ('sub_total', models.DecimalField(default=10.0, max_digits=1000, decimal_places=2)),
                ('tax_total', models.DecimalField(default=10.0, max_digits=1000, decimal_places=2)),
                ('final_total', models.DecimalField(default=10.0, max_digits=1000, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(to='Carts.Cart')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
