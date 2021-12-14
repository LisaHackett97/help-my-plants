""" Url path for articles views """
from django.urls import path
from .import views


urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('getServiceOne/', views.getServiceOne, name='getServiceOne'),
    path('getServiceTwo/', views.getServiceTwo, name='getServiceTwo'),
    path('getServiceThree/', views.getServiceThree, name='getServiceThree'),
]
