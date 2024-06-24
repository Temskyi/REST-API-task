from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import PersonViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'team', TeamViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(router.urls)),
]
