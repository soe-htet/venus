# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(default=10.0, max_digits=2000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(default=10.0, max_digits=2000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(default=10.0, max_digits=2000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'Started', max_length=200, choices=[(b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')]),
        ),
    ]
