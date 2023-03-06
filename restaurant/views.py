from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer, UserSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer    

class userView(APIView):
    
    def get(self, request): 
        items = User.objects.all()
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    