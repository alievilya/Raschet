from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='part3.html')),
    path('page2/', TemplateView.as_view(template_name='Page32.html')),
    path('Page3/', TemplateView.as_view(template_name='Page33.html')),
    path('Page4/', TemplateView.as_view(template_name='Page34.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

