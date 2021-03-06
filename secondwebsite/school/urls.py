from django.urls import path

from . import views
from django.contrib.auth.views import login,logout


app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('subjects/', views.subjects, name='subjects'),
    path('fees/', views.fees, name='fees'),
    path('addClass/', views.addClass, name='addClass'),
    path('addSubject/', views.addSubject, name='addSubject'),
    path('addFee/', views.addFee, name='addFee'),
    path('<int:class_id>/deleteClass', views.deleteClass, name='deleteClass'),
    path('<int:subject_id>/deleteSubject', views.deleteSubject, name='deleteSubject'),
    path('<int:fee_id>/deleteFee', views.deleteFee, name='deleteFee'),
    path('login/', login, {'template_name': 'school/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout')
]