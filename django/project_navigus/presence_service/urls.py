from django.urls import path
from . import views
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
path('signup/', views.SignupView, name='signup'), 
path('login/', views.user_login, name = 'login'),
path('', views.IndexView.as_view(), name='index'),
path('<int:pk>/', views.DocDetailView.as_view(), name='details'),
path('<int:pk>/title/', views.read, name='read'),
path('', views.upload, name='upload'),
]
