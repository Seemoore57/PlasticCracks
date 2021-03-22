from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('output.html', views.output, name='output'),
]