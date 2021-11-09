from django.contrib import admin
from django.urls import path

from .views import LoginView,RegisterView,Plot,SetPermission

urlpatterns = [
    path('main/',Plot.as_view(),name='main'),
    path('login/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('permission/', SetPermission.as_view(), name='permission'),

]
