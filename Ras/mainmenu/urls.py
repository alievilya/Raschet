from django.urls import path, include
from . import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='mainmenu.html')),
    path('part4/', TemplateView.as_view(template_name='part4.html')),
    path('part3/', TemplateView.as_view(template_name='part3.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#path(r'', views.mainmenu, name='mainmenu'),
