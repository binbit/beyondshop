# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beyond', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pictures',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='pictures', to='beyond.Order', null=True),
        ),
    ]
