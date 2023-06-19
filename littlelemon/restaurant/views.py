from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User

from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer, UserSerializer

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def Index(request):
    return render(request, 'index.html',{})

class bookingview(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    perssion_classes = [permissions.IsAuthenticated]
    
    
    
    

    
    

