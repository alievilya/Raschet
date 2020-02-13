from django.shortcuts import render
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import generics

def page1(request):
    return render(request, 'part3/Page1.html')

class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer



