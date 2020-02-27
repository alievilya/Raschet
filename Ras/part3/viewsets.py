from rest_framework import viewsets, filters
from .models import Part3, Part3_2, Part3_3
from .serializers import Part3Serializer, Part3_2Serializer, Part3_3Serializer


class Part3ViewSet(viewsets.ModelViewSet):
    queryset = Part3.objects.all()
    serializer_class = Part3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part3_id', 'Elements', 'Out1')

class Part3_2ViewSet(viewsets.ModelViewSet):
    queryset = Part3_2.objects.all()
    serializer_class = Part3_2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part3_2_id', 'Sc', 'Smax', 'Out2')

class Part3_3ViewSet(viewsets.ModelViewSet):
    queryset = Part3_3.objects.all()
    serializer_class = Part3_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part3_3_id', 'Nvapp', 'Nap', 'Peffpvo', 'Peffreb', 'Out3')

