from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes', views.classes, name='classes'),
    path('subjects', views.subjects, name='subjects'),
    path('fees', views.fees, name='fees'),
]