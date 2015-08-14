# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImageProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=b'', upload_to=b'')),
                ('thumb', models.ImageField(default=b'', null=True, upload_to=b'', blank=True)),
                ('Main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('total_cost', models.IntegerField()),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=1000, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(3, b'completed'), (1, b'pending'), (2, b'processing'), (4, b'shipped')])),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('cost', models.PositiveIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='beyond.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_size', models.IntegerField(default=0)),
                ('y_size', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='size',
            field=models.ForeignKey(to='beyond.Size', null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(to='beyond.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='picture',
            field=models.OneToOneField(to='beyond.Picture'),
        ),
        migrations.AddField(
            model_name='order',
            name='pictures',
            field=models.ManyToManyField(to='beyond.OrderItem'),
        ),
        migrations.AddField(
            model_name='imageproperty',
            name='picture',
            field=models.ForeignKey(related_name='images', to='beyond.Picture'),
        ),
    ]
