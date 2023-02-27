from django.urls import path

from . import views


app_name = 'sampleapp'
urlpatterns = [
    path('', views.index, name='index')
]
