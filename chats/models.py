from django.contrib.auth import get_user_model
from django.db import models
from rooms.models import Room


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(to=get_user_model(), related_name='writer', on_delete=models.CASCADE)
    message = models.TextField(null=False)
    send_time = models.DateTimeField(auto_now=True)

    room_id = models.ForeignKey(to=Room, related_name='room_id', on_delete=models.CASCADE)
