from django.urls import path, include
from rest_framework import routers

from users.views import TestAPI, UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', TestAPI.as_view()),
]