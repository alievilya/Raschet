from rest_framework import viewsets, filters
from .models import Part1, Part1_2, Part1_3
from .serializers import Part1Serializer, Part1_2Serializer, Part1_3Serializer


class Part1ViewSet(viewsets.ModelViewSet):
    queryset = Part1.objects.all()
    serializer_class = Part1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_id', 'Elements', 'Out1')

class Part1_2ViewSet(viewsets.ModelViewSet):
    queryset = Part1_2.objects.all()
    serializer_class = Part1_2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_2_id', 'Sc', 'Smax', 'Out2')

class Part1_3ViewSet(viewsets.ModelViewSet):
    queryset = Part1_3.objects.all()
    serializer_class = Part1_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_3_id', 'Nvapp', 'Nap', 'Peffpvo', 'Peffreb', 'Out3')

