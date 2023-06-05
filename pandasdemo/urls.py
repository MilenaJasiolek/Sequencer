from django.urls import path
from . import views

# Defining URL patterns
urlpatterns = [
    path('', views.home, name="home")
]