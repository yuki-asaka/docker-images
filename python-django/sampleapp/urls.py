from django.urls import path

from . import views


app_name = 'sampleapp'
urlpatterns = [
    path('', views.index, name='index'),

    path('calculate/add', views.add, name='add'),
    path('calculate/divide', views.divide, name='divide'),
]
