from django.urls import include, path
from rest_framework import routers
from user import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from user.views import MyTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from emyxin import views as emyxin_views
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework.documentation import include_docs_urls


router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'checkin',emyxin_views.CheckinViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('docs/',include_docs_urls()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/info',views.get_user_info),
    path('user/token_refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/logout', views.user_logout),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)