
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    #path('api/', include('part3.urls')),
    path('admin/', admin.site.urls),
    path(r'', include('start.urls')),


]
