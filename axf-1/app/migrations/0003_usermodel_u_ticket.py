# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mainshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='u_ticket',
            field=models.CharField(max_length=30, null=True),
        ),
    ]