# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-14 18:06
import annoying.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_add_banned_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='allow_ads',
            field=models.BooleanField(default=True, help_text='If unchecked, you will still see community ads.', verbose_name='See paid advertising'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
