# Generated by Django 4.2.2 on 2023-06-16 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0003_sms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SMS',
        ),
    ]
