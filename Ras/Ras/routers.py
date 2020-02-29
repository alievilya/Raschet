
from rest_framework import routers
from part1.viewsets import Part1ViewSet, Page1BezRazdelViewSet, Part1_3ViewSet
from part2.viewsets import Part2ViewSet, Part2_2ViewSet
from part3.viewsets import Part3ViewSet, Part3_2ViewSet, Part3_3ViewSet
from part4.viewsets import Part4ViewSet, Part4_2ViewSet, Part4_3ViewSet

router = routers.DefaultRouter()

router.register(r'part1_Page1', Part1ViewSet)
router.register(r'page1_br', Page1BezRazdelViewSet)
router.register(r'part1_3', Part1_3ViewSet)

router.register(r'part2', Part2ViewSet)
router.register(r'part2_2', Part2_2ViewSet)

router.register(r'part3', Part3ViewSet)
router.register(r'part3_2', Part3_2ViewSet)
router.register(r'part3_3', Part3_3ViewSet)

router.register(r'part4', Part4ViewSet)
router.register(r'part4_2', Part4_2ViewSet)
router.register(r'part4_3', Part4_3ViewSet)
#router.register(r'', MainmenuViewSet)


