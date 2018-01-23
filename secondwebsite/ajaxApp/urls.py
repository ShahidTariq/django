from django.urls import path

from . import views

app_name = 'ajaxApp'
urlpatterns = [
    path('', views.index, name='index'),
    #path('/resource.json','' , name='resouce'),
]