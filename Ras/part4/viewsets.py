# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 22:52:38
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-04-24 03:37:47
from rest_framework import viewsets, filters
from .models import Part4
from .serializers import Part4Serializer


class Part4ViewSet(viewsets.ModelViewSet):
    queryset = Part4.objects.all()
    serializer_class = Part4Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('part4_line', 'part4_canal', 'part4_number_val')
