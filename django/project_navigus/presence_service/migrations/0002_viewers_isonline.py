# Generated by Django 3.0.8 on 2020-07-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewers',
            name='isonline',
            field=models.BooleanField(default=False),
        ),
    ]
