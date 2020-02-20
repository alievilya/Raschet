
from rest_framework import viewsets, filters
from .models import Part2, Part2_2
from .serializers import Part2Serializer, Part2_2Serializer


class Part2ViewSet(viewsets.ModelViewSet):
    queryset = Part2.objects.all()
    serializer_class = Part2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part2_id', 'Nel', 'res1')

class Part2_2ViewSet(viewsets.ModelViewSet):
    queryset = Part2_2.objects.all()
    serializer_class = Part2_2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part2_2_id', 'Nvskrap', 'Napp', 'res2')




