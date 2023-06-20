from rest_framework import serializers
from .models import Users, user_role, Device, Messages, Services, services_team, history, permission


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'user_email', 'user_phone', 'role', 'approved_status', 'created_at', 'updated_at', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            user_email=validated_data['user_email'],
            user_phone=validated_data['user_phone'],
            role=validated_data['role'],
            approved_status=validated_data['approved_status'],
            password=validated_data['password']
        )
        return user

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_role
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServicesTeamSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = services_team
        fields = ['services_team_id', 'service_id', 'team_id', 'description', 'created_at', 'updated_at', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        team = services_team.objects.create(
            services_team_id=validated_data['services_team_id'],
            service_id=validated_data['service_id'],
            team_id=validated_data['team_id'],
            description=validated_data['description'],
            password=validated_data['password']
        )
        return team

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = permission
        fields = '__all__'
