
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view())  #as_view() function gives the view for the given class
]