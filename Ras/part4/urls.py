from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='part4.html')),
    path('page2/', TemplateView.as_view(template_name='Page42.html')),
    path('page3/', TemplateView.as_view(template_name='Page43.html')),
    path('page4/', TemplateView.as_view(template_name='Page44.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

