# Generated by Django 3.2.8 on 2022-01-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('send_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]