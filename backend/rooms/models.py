from django.contrib.auth import get_user_model
from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=5)
    background_image = models.ImageField(null=True, blank=True)


class Member(models.Model):
    member = models.ForeignKey(primary_key=True, to=get_user_model(), related_name="member", on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, related_name="room", on_delete=models.CASCADE)
