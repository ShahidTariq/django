from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('tech/', include('tech.urls')),
    path('polls/', include('polls.urls')),
    path('school/', include('school.urls')),
]
