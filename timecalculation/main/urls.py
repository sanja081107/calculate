from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('calculation/', calculation, name='calculation'),
]