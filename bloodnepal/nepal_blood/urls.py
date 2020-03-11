"""bloodnepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path    #imported for the regular expression
from . import views                     #imported the views.py files here for our pipeline
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    re_path(r'^$',views.home,name="Homepage"),
    re_path(r'home.html/$',views.home,name="Homepage"),
    re_path(r'donate.html/$',views.donate,name="Donatepage"),
    re_path(r'organization.html/$',views.organization,name="Organizationpage"),
    re_path(r'getinvolved.html/$',views.getinvolved,name="Getinvolvedpage"),
    re_path(r'about.html/$',views.about,name="AboutUspage"),
    re_path(r'carrerwithus.html/$',views.carrer_with_us,name="CarrerWiths"),
    re_path(r'joinhands.html/$',views.joinhands,name="JoinHands"),
    re_path(r'chart.html/$',views.chartView.as_view(),name="Charts"),
    re_path(r'requestBlood.html/$',views.req,name="Request Blood"),
] 
urlpatterns += staticfiles_urlpatterns()
