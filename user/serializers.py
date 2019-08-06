from django.contrib.auth.models import Group
from user.models import UserProfile as User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','password','first_name','last_name', 'groups','avatar','role']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print('in MyTokenObtainPairSerializer')
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['code'] = 20000
        print(token)
        # ...
        # print(token)
        return token
    def validate(self,attrs):
        data = super().validate(attrs)
        re_data={}
        re_data['data']=data
        re_data['code']=20000
        re_data['message']='success'

        return re_data



