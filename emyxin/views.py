from django.shortcuts import render
from rest_framework import viewsets
from emyxin.models import checkinlist
from emyxin.serializers import CheckinlistSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# from emyxin.WXBizDataCrypt import WXBizDataCrypt
import requests
import json


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

    def create(self, request, *args, **kwargs):
        savedata=request.data
        print('savedata is :{0}'.format(savedata))
        scode=savedata['code']
        # encryptedData=savedata['encryptedData']
        # iv=savedata['iv']
        # appid='wxeaf2c5aa3ac7dad2'
        secretcode=self._getSecret(scode)
        # print('scode:{0}'.format(scode))
        # pc = WXBizDataCrypt(appid, secretcode)
        # new_uuid=pc.decrypt(encryptedData, iv)
        if 'openid' in secretcode:
            new_uuid=secretcode['openid']
            print('new_uuid is :{0}'.format(new_uuid))
            savedata['unid']=new_uuid
        else:
            return Response(secretcode, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=savedata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _getSecret(self,code):
        data='https://api.weixin.qq.com/sns/jscode2session?appid=wxeaf2c5aa3ac7dad2&secret=7071e10b2f452d7b899d7dae06022ef9&js_code='+code+'&grant_type=authorization_code'
        r = requests.get(url=data)    # 最基本的GET请求
        print(r.text)
        
        return json.loads(r.text)
        

    

