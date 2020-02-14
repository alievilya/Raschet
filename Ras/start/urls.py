from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='start.html')),
    path(r'mainmenu/', include('mainmenu.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
