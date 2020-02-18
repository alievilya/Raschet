
from rest_framework import viewsets, filters
from .models import Part4, Part4_2, Part4_3
from .serializers import Part4Serializer, Part4_2Serializer, Part4_3Serializer


class Part4ViewSet(viewsets.ModelViewSet):
    queryset = Part4.objects.all()
    serializer_class = Part4Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part4_id', 'line_selected', 'canal_selected', 'number_val', 'cur')

class Part4_2ViewSet(viewsets.ModelViewSet):
    queryset = Part4_2.objects.all()
    serializer_class = Part4_2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part4_2_id', 'mestnost_selected', 'temp_val', 'snow_val', 'wind_val', 'all')

class Part4_3ViewSet(viewsets.ModelViewSet):
    queryset = Part4_3.objects.all()
    serializer_class = Part4_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part4_3_id', 'stanciya_selected', 'marsh_val', 'full')


