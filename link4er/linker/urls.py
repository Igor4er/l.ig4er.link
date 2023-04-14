from django.urls import path
from .views import *

urlpatterns = [
    path('<redirect>/', redirection, name='redirect'),
]
