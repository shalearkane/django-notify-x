# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 07:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='actor_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to='contenttypes.ContentType', verbose_name='Content type of actor object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='actor_object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID of the actor object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='actor_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Anonymous text for actor'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='actor_url_text',
            field=models.URLField(blank=True, null=True, verbose_name='Anonymous URL for actor'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Soft delete status'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description of the notification'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='extra',
            field=models.JSONField(blank=True, null=True, verbose_name='JSONField to store addtional data'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='nf_type',
            field=models.CharField(default='default', max_length=20, verbose_name='Type of notification'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='obj_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_object', to='contenttypes.ContentType', verbose_name='Content type of action object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='obj_object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID of the target object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='obj_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Anonymous text for action object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='obj_url_text',
            field=models.URLField(blank=True, null=True, verbose_name='Anonymous URL for action object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Read status'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='Notification receiver'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType', verbose_name='Content type of target object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID of the target object'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Anonymous text for target'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_url_text',
            field=models.URLField(blank=True, null=True, verbose_name='Anonymous URL for target'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='verb',
            field=models.CharField(max_length=50, verbose_name='Verb of the action'),
        ),
    ]
