# Generated by Django 4.0.3 on 2022-08-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Описание проекта'),
        ),
    ]
