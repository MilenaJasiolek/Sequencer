from django.urls import path
from . import views

# Defining URL patterns
urlpatterns = [
    path('', views.home, name="home"),
    path('dog', views.dog, name="dog"),
    path('cat', views.cat, name="cat"),
    path('other', views.other, name="other"),
    path('info', views.info, name='info'),
]