from django.urls import path, include
from part4 import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
        path('', views.page1, name='start'),
        path('Page1.js/', views.str1),
        path('page2/', views.page2),
        path('page2/Page1.js/', views.str2),
        path('page3/', views.page3),
        path('page4/', views.page4),
        path('test_count/', views.SubscriptionList.as_view()),
        path('test_count/<int:pk>/', views.SubscriptionDetail.as_view()),

 ]

