from django.shortcuts import render
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import generics


class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

def page1(request):
    return render(request, 'part4/Page1/Page1.html')
def str1(request):
    return render(request, 'part4/Page1/Page1.js')

def page2(request):


    return render(request, 'part4/Page2.html', context)

def str2(request):
    return render(request, 'part4/Page1/Page1.js')

def page3(request):
    return render(request, 'part4/Page3.html')


def page4(request):
    #Ttr = (Tm + Tr + Tnr_obsh + Tsau_obsh)*(1 + Kfgu)
    return render(request, 'part4/Page4.html')

import random
import json

def test_vue(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")
    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20,80),
        })

    context = {}
    values = ("bob", "dan", "jack", "lizzy", "susan")

    context["values"] = json.dumps(values)
    context["items_json"] = json.dumps(items)

    return render(request, 'part4/test_vue.html', context)
