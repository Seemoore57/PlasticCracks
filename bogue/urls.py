from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result.html', views.calculate, name='result'),
    path('compare.html', views.calculate, name='compare'),
    path('compare2.html', views.calculate, name='compare2')
]

