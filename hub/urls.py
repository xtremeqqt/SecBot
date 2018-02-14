from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('overview/', views.overview, name='overview'),
    path('networksettings/', views.networksettings, name='networksettings'),
    path('idssettings/', views.idssettings, name='idssettings'),
    path('scanresults/', views.scan, name='scan'),
    path('idsresults/', views.idsresults, name='idsresults'),
    path('dns/', views.dns, name='dns'),

]
