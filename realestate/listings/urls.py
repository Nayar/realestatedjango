from django.urls import path
from .views import *

urlpatterns = [
    # run index function from views.py when we go on path ''
    path('', index, name="index" ),
]
