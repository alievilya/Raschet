from rest_framework import viewsets, filters
from .models import Mainmenu
from .serializers import MainmenuSerializer


class PMainmenuViewSet(viewsets.ModelViewSet):
    queryset = Mainmenu.objects.all()
    serializer_class = MainmenuSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part4_id', 'part4_heading', 'part4_body')