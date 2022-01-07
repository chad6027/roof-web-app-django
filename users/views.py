from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenVerifyView

from users.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet, TokenVerifyView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    
class TestAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer