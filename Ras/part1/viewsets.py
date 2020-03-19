from rest_framework import viewsets, filters
from .models import Part1, Page1BezRazdel, Part1_3

from .models import Page1TimeMarsh, Page1Recogn, Page1BezSostav, Page1TimeRazv
from .serializers import Part1Serializer, Page1BezRazdelSerializer, Page1OneWay1Serializer
from .serializers import Part1_3Serializer
from .serializers import Page1TimeMarshSerializer, Page1TimeRazvSerializer, Page1RecognSerializer, Page1BezSostavSerializer

from .models import Page1OneWay1, Page1Recogn1, Page1TimeRazv1, Page1RazOneSostav1, Page1TimeMarsh1
from .serializers import Page1TimeMarsh1Serializer, Page1TimeRazv1Serializer, Page1Recogn1Serializer, Page1RazOneSostav1Serializer
from .serializers import Page1OneWay1Serializer


from .models import Page1CoupleWays1, Page1Recogn2, Page1TimeRazv2, Page1RazCoupleSostav1, Page1TimeMarsh2
from .serializers import Page1TimeMarsh2Serializer, Page1TimeRazv2Serializer, Page1Recogn2Serializer, Page1RazCoupleSostav1Serializer
from .serializers import Page1CoupleWays1Serializer,Page1CoupleWays1Serializer

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

class Page1BezSostavViewSet(viewsets.ModelViewSet):
    queryset = Page1BezSostav.objects.all()
    serializer_class = Page1BezSostavSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1BezSostav_id', 'SumTimeDay', 'SumTimeNight')

class Page1RecognViewSet(viewsets.ModelViewSet):
    queryset = Page1Recogn.objects.all()
    serializer_class = Page1RecognSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1Recogn_id', 'chasov', 'mins', 'Trecogn')

class Page1TimeMarshViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeMarsh.objects.all()
    serializer_class = Page1TimeMarshSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Tm', 'Tmbez', 'TimeMarsh')

class Page1TimeRazvViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeRazv.objects.all()
    serializer_class = Page1TimeRazvSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1TimeRazv_id', 'Trazv', 'Tsvert', 'TimeRazv')




class Page1OneWay1ViewSet(viewsets.ModelViewSet):
    queryset = Page1OneWay1.objects.all()
    serializer_class = Page1OneWay1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Kir', 'OneWay1Kir')

class Page1RazOneSostav1ViewSet(viewsets.ModelViewSet):
    queryset = Page1RazOneSostav1.objects.all()
    serializer_class = Page1RazOneSostav1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1BezSostav_id', 'SumTimeDay', 'SumTimeNight')

class Page1Recogn1ViewSet(viewsets.ModelViewSet):
    queryset = Page1Recogn.objects.all()
    serializer_class = Page1RecognSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1Recogn_id', 'chasov', 'mins', 'Trecogn')

class Page1TimeMarsh1ViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeMarsh1.objects.all()
    serializer_class = Page1TimeMarsh1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Tm', 'Tmbez', 'TimeMarsh')

class Page1TimeRazv1ViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeRazv1.objects.all()
    serializer_class = Page1TimeRazv1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1TimeRazv_id', 'Trazv', 'Tsvert', 'TimeRazv')





class Page1CoupleWays1ViewSet(viewsets.ModelViewSet):
    queryset = Page1CoupleWays1.objects.all()
    serializer_class = Page1CoupleWays1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Kir', 'OneWay1Kir')

class Page1RazCoupleSostav1ViewSet(viewsets.ModelViewSet):
    queryset = Page1RazCoupleSostav1.objects.all()
    serializer_class = Page1RazCoupleSostav1Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1BezSostav_id', 'SumTimeDay', 'SumTimeNight')

class Page1Recogn2ViewSet(viewsets.ModelViewSet):
    queryset = Page1Recogn2.objects.all()
    serializer_class = Page1Recogn2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1Recogn_id', 'chasov', 'mins', 'Trecogn')

class Page1TimeMarsh2ViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeMarsh2.objects.all()
    serializer_class = Page1TimeMarsh2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1OneWay1_id', 'Tm', 'Tmbez', 'TimeMarsh')

class Page1TimeRazv2ViewSet(viewsets.ModelViewSet):
    queryset = Page1TimeRazv2.objects.all()
    serializer_class = Page1TimeRazv2Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Page1TimeRazv_id', 'Trazv', 'Tsvert', 'TimeRazv')



class Part1_3ViewSet(viewsets.ModelViewSet):
    queryset = Part1_3.objects.all()
    serializer_class = Part1_3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part1_3_id', 'Nvapp', 'Nap', 'Peffpvo', 'Peffreb', 'Out3')

