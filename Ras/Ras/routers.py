# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 23:08:11
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-02-04 23:25:39
from rest_framework import routers
from part3.viewsets import Part3ViewSet, Part3_2ViewSet, Part3_3ViewSet
from part4.viewsets import Part4ViewSet, Part4_2ViewSet, Part4_3ViewSet
from part2.viewsets import Part2ViewSet, Part2_2ViewSet
router = routers.DefaultRouter()

router.register(r'part2', Part2ViewSet)
router.register(r'part2_2', Part2_2ViewSet)

router.register(r'part3', Part3ViewSet)
router.register(r'part3_2', Part3_2ViewSet)
router.register(r'part3_3', Part3_3ViewSet)

router.register(r'part4', Part4ViewSet)
router.register(r'part4_2', Part4_2ViewSet)
router.register(r'part4_3', Part4_3ViewSet)
#router.register(r'', MainmenuViewSet)


