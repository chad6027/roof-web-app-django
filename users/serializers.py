from django.db import transaction
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    artist_name = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=30)
    gender = serializers.CharField(max_length=30)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.artist_name = self.data.get('artist_name')
        user.nickname = self.data.get('nickname')
        user.gender = self.data.get('gender')
        user.save()
        return user