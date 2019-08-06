from django.contrib.auth.models import Group
from user.models import UserProfile as User
from rest_framework import viewsets
from user.serializers import UserSerializer, GroupSerializer,MyTokenObtainPairSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse,JsonResponse
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth import get_user_model

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


def get_user_info(request):

    User = get_user_model()
    if request.method=='GET':
        print("in get")
        # print(dir(request))
        #获取请求参数token的值
        token=request.headers.get('AUTHORIZATION')
        # test=request.META.get('CONTENT-TYPE')
        # print(test)
        # print(token)

        token_msg=authentication.JWTAuthentication().get_validated_token(token)
        print(token_msg)
        user_object=authentication.JWTAuthentication().get_user(token_msg)
        # # print(dir(user_a))
        # # #顶一个空数组来接收token解析后的值
        # # toke_user = []
        # # toke_user = jwt_decode_handler(token)
        # # #获得user_id
        # # user_id = toke_user["user_id"]
        # # #通过user_id查询用户信息
        # user_info = User.objects.get(pk= user_id)
        # serializer = UserSerializer(user_info)
        # User_info=UserSerializer(user_object.id).data
        # print(User_info)
        data = {"username":user_object.username,
                     "first_name":user_object.first_name,
                     "last_name": user_object.last_name,
                     "avatar":user_object.avatar,
                    #  "groups":user_object.groups,
                     "roles":user_object.role,
                     "introduction":user_object.introduction         
        }
        re_data={"data": data,
                 "code": 20000,
                 "message": "success"
        }
        return JsonResponse(re_data)
