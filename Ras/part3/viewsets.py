# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 22:52:38
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-04-24 03:37:47
from rest_framework import viewsets, filters
from .models import Part3
from .serializers import Part3Serializer


class Part3ViewSet(viewsets.ModelViewSet):
    queryset = Part3.objects.all()
    serializer_class = Part3Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part3_id', 'part3_heading', 'part3_body')
