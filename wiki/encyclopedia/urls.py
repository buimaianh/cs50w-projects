from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/random_page/', views.random_page, name='random_page'),
    path('wiki/<str:entry>/edit/', views.edit_page, name='edit_page'),
    path('wiki/new_page/', views.new_page, name='new_page'),
    path('wiki/search/', views.search, name='search'),
    path('wiki/<str:title>/', views.entry, name='entry'),
]