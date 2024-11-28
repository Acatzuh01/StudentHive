from django.urls import path
from . import views  # Import views from the students app

urlpatterns = [
    # Define the URL patterns for the students app
    path('', views.list_students, name='students_list'),  # Example view to list students
]
