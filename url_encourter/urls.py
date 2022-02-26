from django.shortcuts import redirect
from django.urls import path
from url_encourter import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_url', views.new_url, name='new_url'),
    path('<token>', views.load_url, name='redirect'),
]
