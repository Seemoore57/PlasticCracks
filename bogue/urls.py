from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result.html', views.calculate, name='result'),
    path('compare.html', views.compare, name='compare'),
    path('compare2.html', views.compare2, name='compare2')
]

