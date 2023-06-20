# Generated by Django 4.2.2 on 2023-06-15 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('user_name', models.CharField(default='', max_length=45)),
                ('device_name', models.CharField(max_length=45)),
                ('device_quantity', models.IntegerField(default=0)),
                ('cost', models.CharField(default=None, max_length=45, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Device',
            },
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('sent_numbers', models.IntegerField(null=True)),
                ('replied_numbers', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'history',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('device_id', models.IntegerField()),
                ('message_title', models.CharField(max_length=45, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='permission',
            fields=[
                ('permission_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('services_name', models.CharField(max_length=45)),
                ('user_id', models.IntegerField(default=0)),
                ('services_title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('device_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Services',
            },
        ),
        migrations.CreateModel(
            name='services_team',
            fields=[
                ('services_team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('service_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('description', models.CharField(max_length=45, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'services_team',
            },
        ),
        migrations.CreateModel(
            name='user_role',
            fields=[
                ('user_role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('user_email', models.CharField(max_length=45)),
                ('user_phone', models.FloatField()),
                ('role', models.IntegerField()),
                ('approved_status', models.SmallIntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]