from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results.html', views.calculate, name='result')
]