# Generated by Django 4.0 on 2021-12-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='origin',
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
