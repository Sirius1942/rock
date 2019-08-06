from django.urls import include, path
from rest_framework import routers
from user import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from user.views import MyTokenObtainPairView
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/info',views.get_user_info),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]