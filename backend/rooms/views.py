import http

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.models import Room, Member
from rooms.serializers import RoomSerializer


class RoomList(APIView):

    def get(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_room = Room.objects.create(data=self.request.data)
        new_member = Member.objects.create(member=self.request.user, room=new_room)

        return Response(status=status.HTTP_200_OK)
