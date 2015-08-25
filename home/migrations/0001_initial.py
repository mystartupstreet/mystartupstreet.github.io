# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=100)),
                ('post_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_likes', models.IntegerField(default=0)),
                ('post_comments', models.CharField(max_length=200)),
                ('post', models.ForeignKey(to='home.Posts')),
            ],
        ),
    ]
