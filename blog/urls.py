from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.ShowAllBlogs.as_view(), name='all_blogs'),
    path('<slug:slug>/', views.ShowDetailBlog.as_view(), name='detail-post'),
]
