from django.urls import path, include
from part3 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'', views.page1, name='start'),
    path('test_count/', views.SubscriptionList.as_view()),
    path('test_count/<int:pk>/', views.SubscriptionDetail.as_view()),
]

#