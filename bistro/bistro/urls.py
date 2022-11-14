from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from bistro.menus import views

router = routers.DefaultRouter()
router.register(r'menus', views.MenusViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




# import menus

# urlpatterns = [
#     path('', include('menus.urls')),
#     path('admin/', admin.site.urls),