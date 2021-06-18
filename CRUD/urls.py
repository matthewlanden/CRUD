
from django.urls import path
from.views import *

urlpatterns = [
    path('', home, name='homeindex'),
    path('update/<str:itemId>', update, name='updateindex'),
    path('delete/<str:itemId>', delete, name='deleteindex'),
    path('ok/<str:itemId>', ok, name='okindex'),
]

