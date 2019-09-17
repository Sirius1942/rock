from django.shortcuts import render
from rest_framework import viewsets
from emyxin.models import checkinlist
from emyxin.serializers import CheckinlistSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication

# Create your views here.
class CheckinViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    permission_classes = [permissions.AllowAny]
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = checkinlist.objects.all()
    serializer_class = CheckinlistSerializer