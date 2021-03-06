# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151019_1121'),
        ('digi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themepage',
            name='blog_category',
            field=models.ForeignKey(blank=True, help_text='Corresponding blog category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='themepage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()),), blank=True, null=True),
        ),
    ]
