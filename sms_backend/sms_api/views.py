from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Users, user_role, Device, Messages, Services, services_team, history, permission
from .serializers import UsersSerializer, UserRoleSerializer, DeviceSerializer, MessagesSerializer, ServicesSerializer, ServicesTeamSerializer, HistorySerializer, PermissionSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserSignupAPIView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = user_role.objects.all()
    serializer_class = UserRoleSerializer


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_role.objects.all()
    serializer_class = UserRoleSerializer


class DeviceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # Admin acces
    permission_classes = [IsAdminUser]



class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesTeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = services_team.objects.all()
    serializer_class = ServicesTeamSerializer


class ServicesTeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = services_team.objects.all()
    serializer_class = ServicesTeamSerializer


class ServicesTeamLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        services_team = authenticate(username=username, password=password)
        if services_team is not None:
            login(request, services_team)
            refresh = RefreshToken.for_user(services_team)

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ServicesTeamSignupAPIView(APIView):
    def post(self, request):
        serializer = ServicesTeamSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            refresh = RefreshToken.for_user(team)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = history.objects.all()
    serializer_class = HistorySerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

# Apply the `IsAuthenticated` permission to other relevant views as needed.



class HistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = history.objects.all()
    serializer_class = HistorySerializer


class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer


class PermissionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer
