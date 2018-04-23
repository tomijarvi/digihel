# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-18 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('helsinkioppii', '0021_case_relation_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='content_evaluation',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Evaluation'),
        ),
        migrations.AlterField(
            model_name='case',
            name='content_materials',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Materials'),
        ),
        migrations.AlterField(
            model_name='case',
            name='content_who',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Participants'),
        ),
        migrations.AlterField(
            model_name='case',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helsinkioppii.SchoolGrade', verbose_name='Level of education'),
        ),
        migrations.AlterField(
            model_name='case',
            name='grades',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='_case_grades_+', to='helsinkioppii.SchoolGrade', verbose_name='Levels of education'),
        ),
        migrations.AlterField(
            model_name='case',
            name='school',
            field=models.CharField(blank=True, max_length=128, verbose_name='Educational institution'),
        ),
        migrations.AlterField(
            model_name='case',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helsinkioppii.SchoolSubject', verbose_name='School subject'),
        ),
        migrations.AlterField(
            model_name='case',
            name='subjects',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='_case_subjects_+', to='helsinkioppii.SchoolSubject', verbose_name='School subjects'),
        ),
        migrations.AlterField(
            model_name='case',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helsinkioppii.CaseTheme', verbose_name='Theme'),
        ),
        migrations.AlterField(
            model_name='case',
            name='themes',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='_case_themes_+', to='helsinkioppii.CaseTheme', verbose_name='Themes'),
        ),
        migrations.AlterField(
            model_name='caseattachment',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='casetheme',
            name='theme',
            field=models.CharField(blank=True, max_length=128, verbose_name='Theme'),
        ),
        migrations.AlterField(
            model_name='schoolgrade',
            name='grade',
            field=models.CharField(blank=True, max_length=128, verbose_name='Level of education'),
        ),
        migrations.AlterField(
            model_name='schoolsubject',
            name='subject',
            field=models.CharField(blank=True, max_length=128, verbose_name='School subject'),
        ),
    ]