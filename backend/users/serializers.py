from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import transaction
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomRegisterSerializer(RegisterSerializer):
    user_name = serializers.CharField(max_length=20)
    nickname = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=11)
    birthday = serializers.CharField(max_length=8)
    gender = serializers.CharField()
    profile_image = serializers.ImageField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.user_name = self.data.get('user_name')
        user.nickname = self.data.get('nickname')
        user.phone_number = self.data.get('phone_number')
        user.birthday = self.data.get('birthday')
        user.gender = self.data.get('gender')
        user.profile_image = self.data.get('profile_image')
        user.save()
        return user