from rest_framework import viewsets, filters
from .models import Part1, Page1BezRazdel, Page1OneWay1,Page1OneWay2,Page1CoupleWays1, Page1CoupleWays2, Part1_3
from .serializers import Part1Serializer, Page1BezRazdelSerializer, Page1OneWay1Serializer, Page1OneWay2Serializer
from .serializers import Page1CoupleWays1Serializer, Page1CoupleWays2Serializer, Part1_3Serializer


class Part1ViewSet(viewsets.ModelViewSet):
    queryset = Part1.objects.all()
    serializer_class = Part1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_id', 'Elements', 'Out1')

class Page1BezRazdelViewSet(viewsets.ModelViewSet):
    queryset = Page1BezRazdel.objects.all()
    serializer_class = Page1BezRazdelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1BezRazdel_id', 'Kir', 'BezRazdelKir')

class Page1OneWay1ViewSet(viewsets.ModelViewSet):
    queryset = Page1OneWay1.objects.all()
    serializer_class = Page1OneWay1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Kir', 'OneWay1Kir')

class Page1OneWay2ViewSet(viewsets.ModelViewSet):
    queryset = Page1OneWay2.objects.all()
    serializer_class = Page1OneWay2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay2_id', 'Kir', 'OneWay2Kir')

class Page1CoupleWays1ViewSet(viewsets.ModelViewSet):
    queryset = Page1CoupleWays1.objects.all()
    serializer_class = Page1CoupleWays1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1CoupleWays1_id', 'Kir', 'CoupleWays1Kir')

class Page1CoupleWays2ViewSet(viewsets.ModelViewSet):
    queryset = Page1CoupleWays2.objects.all()
    serializer_class = Page1CoupleWays2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1CoupleWays2_id', 'Kir', 'CoupleWays2Kir')

class Part1_3ViewSet(viewsets.ModelViewSet):
    queryset = Part1_3.objects.all()
    serializer_class = Part1_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_3_id', 'Nvapp', 'Nap', 'Peffpvo', 'Peffreb', 'Out3')

