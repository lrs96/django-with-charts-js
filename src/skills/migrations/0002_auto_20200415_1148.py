# Generated by Django 2.2 on 2020-04-15 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='score',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator('1'), django.core.validators.MaxLengthValidator('5')]),
        ),
    ]
