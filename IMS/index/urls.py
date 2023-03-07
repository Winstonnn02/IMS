from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('search/', search),
    path('change/', change),
    path('auth/', auth),
    path('graphs/', graphs)
]
