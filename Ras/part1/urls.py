from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
#path('Page1/', include('part1.Page1.urls')),
urlpatterns = [
    path(r'', TemplateView.as_view(template_name='part1.html')),
    path('Page1/',  TemplateView.as_view(template_name='Page1/Page1.html')),
    path('Page1BezRazdel/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1BezRazdel.html')),
    path('Page1BezSostav/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1BezSostav.html')),
    path('Page1Recogn/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1Recogn.html')),
    path('Page1TimeMarsh/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1TimeMarsh.html')),
    path('Page1TimeRazv/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1TimeRazv.html')),
    path('Page1Final/', TemplateView.as_view(template_name='Page1/BezRazdel/Page1Final.html')),

    path('Page1Razdel/', TemplateView.as_view(template_name='Page1/Page1Razdel.html')),
    path('Page1Lots/', TemplateView.as_view(template_name='Page1/Page1Lots.html')),
    path('Page1ChangeBD/', TemplateView.as_view(template_name='Page1/Page1ChangeBD.html')),

    path('Page1Razdel/Page1OneWay1/', TemplateView.as_view(template_name='Page1/Razdel1/Page1OneWay1.html')),
    path('Page1Razdel/Page1OneWay2/', TemplateView.as_view(template_name='Page1/Razdel1/Page1OneWay2.html')),
    path('Page1Razdel/Page1RazOneSostav1/', TemplateView.as_view(template_name='Page1/Razdel1/Page1RazOneSostav1.html')),
    path('Page1Razdel/Page1RazOneSostav2/', TemplateView.as_view(template_name='Page1/Razdel1/Page1RazOneSostav2.html')),
    path('Page1Razdel/Page1Recogn1/', TemplateView.as_view(template_name='Page1/Razdel1/Page1Recogn1.html')),
    path('Page1Razdel/Page1Recogn2/', TemplateView.as_view(template_name='Page1/Razdel1/Page1Recogn2.html')),
    path('Page1Razdel/Page1TimeMarsh1/', TemplateView.as_view(template_name='Page1/Razdel1/Page1TimeMarsh1.html')),
    path('Page1Razdel/Page1TimeRazv1/', TemplateView.as_view(template_name='Page1/Razdel1/Page1TimeRazv1.html')),
    path('Page1Razdel/Page1TimeRazv2/', TemplateView.as_view(template_name='Page1/Razdel1/Page1TimeRazv2.html')),
    path('Page1Razdel/Page1OneFinal/', TemplateView.as_view(template_name='Page1/Razdel1/Page1OneFinal.html')),

    path('Page1CoupleWays1/', TemplateView.as_view(template_name='Page1/RazdelCouple/Page1CoupleWays1.html')),
    path('Page1CoupleWays2/', TemplateView.as_view(template_name='Page1/RazdelCouple/Page1CoupleWays2.html')),
    path('Page1RazCoupleSostav/', TemplateView.as_view(template_name='Page1/RazdelCouple/Page1RazCoupleSostav.html')),

    path('Page2/', TemplateView.as_view(template_name='Page2.html')),
    path('Page3/', TemplateView.as_view(template_name='Page13.html')),
    path('Page4/', TemplateView.as_view(template_name='Page14.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

