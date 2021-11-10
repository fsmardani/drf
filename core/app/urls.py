from django.contrib import admin
from django.urls import path

from .views import LoginView,RegisterView,Plot,SetPermission,AccountsList

urlpatterns = [
    path('main/',Plot.as_view(),name='main'),
    path('login/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/',AccountsList.as_view(),name='list'),

    path('permission/<int:pk>', SetPermission.as_view(), name='permission'),

]
