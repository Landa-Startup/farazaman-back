# Generated by Django 4.2.2 on 2024-01-27 12:46

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='logo',
            field=models.ImageField(upload_to='base/logos'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='members',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='startupsubmit',
            name='members_count',
            field=models.PositiveIntegerField(validators=[base.models.positive_validator]),
        ),
    ]
