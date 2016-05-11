# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-11 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayase_blog', '0002_auto_20160511_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callout',
            name='level',
            field=models.CharField(choices=[('N', 'Common Notice'), ('W', 'Warning'), ('D', 'Danger'), ('R', 'Recommend')], max_length=1),
        ),
    ]