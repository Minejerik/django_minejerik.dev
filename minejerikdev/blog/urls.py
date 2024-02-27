from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog_overview'),
    path('<int:blog_id>', views.blog_post, name='blog_post'),
]