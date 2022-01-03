from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from users.managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    artist_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    revenue = models.IntegerField(default=0)

    artist_img = models.ImageField(default='default.jpeg')

    def __str__(self):
        return self.email