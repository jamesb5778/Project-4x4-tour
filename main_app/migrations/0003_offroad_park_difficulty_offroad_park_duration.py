# Generated by Django 4.0 on 2022-01-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_offroad_park_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='offroad_park',
            name='Difficulty',
            field=models.CharField(default='Easy', max_length=100),
        ),
        migrations.AddField(
            model_name='offroad_park',
            name='Duration',
            field=models.CharField(default='1 hour', max_length=100),
        ),
    ]
