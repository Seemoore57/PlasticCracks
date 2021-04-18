from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pcgraphs.html', views.pcgraphs, name='pcgraphs')
]