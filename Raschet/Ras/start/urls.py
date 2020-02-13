from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.start, name='start'),
    path(r'mainmenu/', include('mainmenu.urls'))
]
