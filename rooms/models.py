from django.db import models

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=5)
    background_image = models.ImageField(null=True, blank=True)


