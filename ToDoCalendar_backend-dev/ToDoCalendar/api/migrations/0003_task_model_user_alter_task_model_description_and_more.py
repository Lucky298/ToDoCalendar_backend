# Generated by Django 4.0.5 on 2022-06-17 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_task_model_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db
                                    .models.deletion.CASCADE,
                                    related_name='tasks',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='description',
            field=models.TextField(blank=True, null=True,
                                   verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='end_date',
            field=models.DateTimeField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
