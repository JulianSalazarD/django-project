from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.menu, name="menu"),
    path('menu_item/', views.menu_item, name="menu_item")
]