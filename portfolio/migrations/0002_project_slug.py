# Generated by Django 4.0.3 on 2022-08-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]