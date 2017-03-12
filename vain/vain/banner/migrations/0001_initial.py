# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('link_url', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('order_no', models.IntegerField(null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
