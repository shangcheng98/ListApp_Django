from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.logins, name='logins'),
    path('login', views.logins, name='logins'),
    path('mylist', views.mylist, name='mylist'), 
    path('index', views.index, name='index'),  
    path('logout', views.log_out, name='logout'),  
    
]