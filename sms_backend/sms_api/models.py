from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.hashers import make_password

class CustomGroup(Group):
    class Meta:
        proxy = True

class CustomPermission(Permission):
    class Meta:
        proxy = True

class Users(AbstractUser):
    user_email = models.CharField(max_length=45)
    user_phone = models.FloatField()
    role = models.IntegerField()
    approved_status = models.SmallIntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    # Manually define a default value for the password field
    password = models.CharField(max_length=128, default='')

    def save(self, *args, **kwargs):
        if not self.pk:
            # Hash the password for new user
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    class Meta:
        db_table = 'users'

class user_role(models.Model):
    user_role_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'user_role'


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=45, default="")
    device_name = models.CharField(max_length=45)
    device_quantity = models.IntegerField(default=0)
    cost = models.CharField(max_length=45, null=True, default=None)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Device'


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    device_id = models.IntegerField()
    message_title = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'messages'


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    services_name = models.CharField(max_length=45)
    user_id = models.IntegerField(default=0)
    services_title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    device_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Services'


class services_team(models.Model):
    services_team_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    team_id = models.IntegerField()
    description = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Hash the password for new team
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'services_team'


class history(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    sent_numbers = models.IntegerField(null=True)
    replied_numbers = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'history'


class permission(models.Model):
    permission_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45)

    class Meta:
        db_table = 'permission'
