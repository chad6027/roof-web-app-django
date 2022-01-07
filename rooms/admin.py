from django.contrib import admin

# Register your models here.
from rooms.models import Room, Member

admin.site.register(Room)
admin.site.register(Member)
