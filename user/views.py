from django.contrib.auth.models import Group
from user.models import UserProfile as User
from rest_framework import viewsets
from user.serializers import UserSerializer, GroupSerializer,MyTokenObtainPairSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.

    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
