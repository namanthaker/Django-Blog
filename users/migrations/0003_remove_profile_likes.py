# Generated by Django 3.2.3 on 2021-05-31 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210531_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
    ]