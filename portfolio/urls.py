from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomepageDisplay.as_view(), name='home'),
    path('info_project/<slug:slug>', views.DitailProject.as_view(), name='info_project'),
]
