from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from .models import Booking, MenuItem
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemItemView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
@api_view()
@permission_classes([IsAuthenticated])    
def message(request):
    return Response({"message":"This View is protected"})
