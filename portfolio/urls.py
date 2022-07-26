from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomepageDisplay.as_view(), name='home'),
]