from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
#path('Page1/', include('part1.Page1.urls')),
urlpatterns = [
    path(r'', TemplateView.as_view(template_name='part1.html')),
    path('Page1/',  TemplateView.as_view(template_name='Page1/Page1.html')),
    path('Page1BezRazdel/', TemplateView.as_view(template_name='Page1/Page1BezRazdel.html')),
    path('Page1BezSostav/', TemplateView.as_view(template_name='Page1/Page1BezSostav.html')),

    path('Page1Razdel/', TemplateView.as_view(template_name='Page1/Page1Razdel.html')),
    path('Page1Lots/', TemplateView.as_view(template_name='Page1/Page1Lots.html')),
    path('Page1ChangeBD/', TemplateView.as_view(template_name='Page1/Page1ChangeBD.html')),

    path('Page2/', TemplateView.as_view(template_name='Page2.html')),
    path('Page3/', TemplateView.as_view(template_name='Page13.html')),
    path('Page4/', TemplateView.as_view(template_name='Page14.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

