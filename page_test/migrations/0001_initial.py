# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('token', models.CharField(max_length=250)),
                ('id_page', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=300)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('number_photos', models.IntegerField(blank=True)),
                ('current_photo_id', models.IntegerField(blank=True)),
                ('likes', models.IntegerField(default=0)),
                ('album_cover', models.CharField(default=b'', max_length=30)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_photo', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('likes', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=355)),
                ('company', models.ForeignKey(to='page_test.Company')),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=250)),
                ('id_facebook', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
