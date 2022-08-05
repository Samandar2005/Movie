from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('main/', index, name='main'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('genre/', genre, name='genre'),
]
