from django.db import models
#引入系统用户的分类
from django.contrib.auth.models import AbstractUser

# Create your models here.

#userProfile继承AbstractUser分类，进行拓展
class UserProfile(AbstractUser):
    """
    用户类拓展
    """
    # name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名" )
    avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="avatar")
    role = models.CharField(max_length=10, default="editor", verbose_name="role")
    introduction = models.TextField(max_length=500,null=True,blank=True, verbose_name="introduction")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username