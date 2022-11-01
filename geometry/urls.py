from django.urls import path

from .views import triangle

app_name = 'geometry'
urlpatterns = [
        path('', triangle, name='triangle')
    ]
