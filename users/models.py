from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from users.managers import CustomUserManager

# (stored in DB, Display)
GENDER = [
    ("M", "Male"),
    ("F", "Female")
]


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    user_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    birthday = models.CharField(max_length=8)
    gender = models.CharField(choices=GENDER, default="M", max_length=10)
    nickname = models.CharField(max_length=30)
    profile_image = models.ImageField(default='default.jpeg')
    relation = models.CharField(max_length=20, default="None")

    def __str__(self):
        return self.email