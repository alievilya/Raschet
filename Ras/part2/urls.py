from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='part2.html')),
    path('page2/', TemplateView.as_view(template_name='Page22.html')),
    path('page3/', TemplateView.as_view(template_name='Page23.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

