# Generated by Django 4.0.3 on 2022-08-06 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_portfolioshots_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioshots',
            old_name='shots',
            new_name='image',
        ),
    ]