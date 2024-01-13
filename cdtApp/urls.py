from django.urls import path
from .views import countdown, get_remaining_time

urlpatterns = [
    path('countdown/', countdown, name='countdown'),
    path('get_remaining_time/', get_remaining_time, name='get_remaining_time'),
]