# Generated by Django 3.0.4 on 2020-03-24 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0003_auto_20200324_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharesheld',
            name='owner',
        ),
    ]
