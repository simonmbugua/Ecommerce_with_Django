from django.urls import path
from django.urls import views

urlpatterns = [
    path('', views.home, name='home'),
]