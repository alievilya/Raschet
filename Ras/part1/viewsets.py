from rest_framework import viewsets, filters
from .models import Part1, Page1BezRazdel, Part1_3
from .serializers import Part1Serializer, Page1BezRazdelSerializer, Part1_3Serializer


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

class Part1_3ViewSet(viewsets.ModelViewSet):
    queryset = Part1_3.objects.all()
    serializer_class = Part1_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_3_id', 'Nvapp', 'Nap', 'Peffpvo', 'Peffreb', 'Out3')

