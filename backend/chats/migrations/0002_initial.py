# Generated by Django 3.2.8 on 2022-01-04 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_id', to='rooms.room'),
        ),
        migrations.AddField(
            model_name='chat',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL),
        ),
    ]
