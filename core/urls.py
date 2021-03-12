from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'core'

urlpatterns = [
	path('main/', views.main, name='main_url'),
	path('login/',views.loginPage.as_view(),name='login'),
    path('home/',views.registerPage.as_view())
	
]