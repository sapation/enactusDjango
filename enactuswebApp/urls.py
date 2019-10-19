from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('gallary/', views.gallary, name='gallary'),
    path('blog/', views.blog, name='blog'),   
    path('blog/posts/<slug:slug_text>', views.blog_detail, name='blog_detail'),  
]
