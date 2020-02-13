from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.mainmenu, name='mainmenu'),
    path('part1/', include('part1.urls')),
    path('part2/', include('part2.urls')),
    path('part3/', include('part3.urls')),
    path('part4/', include('part4.urls')),
    path('test_api/', include('part3.urls')),
]