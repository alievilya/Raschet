from rest_framework import routers

from part1.viewsets import Part1ViewSet, Page1BezRazdelViewSet, Page1BezSostavViewSet
from part1.viewsets import Page1TimeMarshViewSet, Page1RecognViewSet, Page1TimeRazvViewSet
#Razdel
from part1.viewsets import Page1TimeMarsh1ViewSet, Page1Recogn1ViewSet, Page1TimeRazv1ViewSet
from part1.viewsets import Page1RazOneSostav1ViewSet, Page1OneWay1ViewSet

#Couple
from part1.viewsets import Page1CoupleWays1ViewSet, Page1RazCoupleSostav1ViewSet, Page1Recogn2ViewSet
from part1.viewsets import Page1TimeMarsh2ViewSet, Page1TimeRazv2ViewSet

from part1.viewsets import Part1_3ViewSet
from part2.viewsets import Part2ViewSet, Part2_2ViewSet
from part3.viewsets import Part3ViewSet, Part3_2ViewSet, Part3_3ViewSet
from part4.viewsets import Part4ViewSet, Part4_2ViewSet, Part4_3ViewSet

router = routers.DefaultRouter()

router.register(r'part1_Page1', Part1ViewSet)
router.register(r'page1_br', Page1BezRazdelViewSet)
router.register(r'page1_bs', Page1BezSostavViewSet)
router.register(r'page1_btrec', Page1RecognViewSet)
router.register(r'page1_btm', Page1TimeMarshViewSet)
router.register(r'page1_btraz', Page1TimeRazvViewSet)

router.register(r'page1_oneway', Page1OneWay1ViewSet)
router.register(r'page1_onesost', Page1RazOneSostav1ViewSet)
router.register(r'page1_onetrec', Page1Recogn1ViewSet)
router.register(r'page1_onetm', Page1TimeMarsh1ViewSet)
router.register(r'page1_onetrazv', Page1TimeRazv1ViewSet)


#router.register(r'page1_ow2', Page1OneWay2ViewSet)

router.register(r'page1_coupleway', Page1CoupleWays1ViewSet)
router.register(r'page1_couplesost', Page1RazCoupleSostav1ViewSet)
router.register(r'page1_coupletrec', Page1Recogn2ViewSet)
router.register(r'page1_coupletm', Page1TimeMarsh2ViewSet)
router.register(r'page1_coupletrazv', Page1TimeRazv2ViewSet)

#router.register(r'page1_cw1', Page1CoupleWays1ViewSet)
#router.register(r'page1_cw2', Page1CoupleWays2ViewSet)

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


