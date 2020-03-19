from django.contrib import admin
from .models import Part1, Part1_3

from .models import Page1BezRazdel, Page1BezSostav, Page1TimeMarsh, Page1Recogn, Page1TimeRazv

#Razdel
from .models import Page1OneWay1, Page1Recogn1, Page1TimeRazv1, Page1RazOneSostav1, Page1TimeMarsh1
#Page1OneWay2, Page1Recogn2, Page1TimeRazv2, Page1RazOneSostav2, Page1Razdel,

#Couple
from .models import Page1CoupleWays1, Page1Recogn2, Page1TimeRazv2, Page1RazCoupleSostav1, Page1TimeMarsh2

admin.site.register(Part1)

admin.site.register(Page1BezRazdel)
admin.site.register(Page1BezSostav)
admin.site.register(Page1TimeMarsh)
admin.site.register(Page1Recogn)
admin.site.register(Page1TimeRazv)


admin.site.register(Page1OneWay1)
admin.site.register(Page1RazOneSostav1)
admin.site.register(Page1TimeMarsh1)
admin.site.register(Page1Recogn1)
admin.site.register(Page1TimeRazv1)
#admin.site.register(Page1Razdel)
#admin.site.register(Page1OneWay2)
#admin.site.register(Page1RazOneSostav2)
#admin.site.register(Page1Recogn2)
#admin.site.register(Page1TimeRazv2)


admin.site.register(Page1CoupleWays1)
admin.site.register(Page1RazCoupleSostav1)
admin.site.register(Page1TimeMarsh2)
admin.site.register(Page1Recogn2)
admin.site.register(Page1TimeRazv2)
#admin.site.register(Page1CoupleWays2)

admin.site.register(Part1_3)


