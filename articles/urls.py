from django.urls import path
from .import views


urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('get_serviceOne/', views.get_serviceOne, name='get_serviceOne'),
    path('get_serviceTwo/', views.get_serviceTwo, name='get_serviceTwo'),
    path('get_serviceThree/', views.get_serviceThree, name='get_serviceThree'),
    
]