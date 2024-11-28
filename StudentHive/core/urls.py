from django.urls import path
from core import views  # Ensure the correct import path

urlpatterns = [
    path('', views.home, name='home'),  # Ensure the correct view is mapped here
]
