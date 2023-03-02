from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

class RoomView(generics.ListAPIView):#this function allows us to create and view the rooms.
    queryset = Room.objects.all() #retrieve all rooms created
    serializer_class = RoomSerializer  #convert the data into some format(json)