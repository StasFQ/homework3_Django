from django.urls import path

from .views import create_person, triangle, update_person

app_name = 'geometry'
urlpatterns = [
        path('', triangle, name='triangle'),
        path('person/', create_person, name='create_person'),
        path('<int:pk>/person/', update_person, name='update_person')
    ]
