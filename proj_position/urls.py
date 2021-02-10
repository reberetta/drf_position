from django.contrib import admin
from django.urls import path, include
from drf_position.position import views 
from rest_framework import routers 

route = routers.DefaultRouter()
router.register(r'position', views.PositionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), namespace='rest_framework')
]