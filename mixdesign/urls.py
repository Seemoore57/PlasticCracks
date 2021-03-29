from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('output_FT.html', views.calculate, name='output1'),
    path('output_M.html', views.calculate, name='output2'),
]