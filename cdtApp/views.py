from django.shortcuts import render
from django.http import JsonResponse
from .models import Countdown
import datetime

def countdown(request):
    countdown_obj = Countdown.objects.first()
    if countdown_obj:
        duration_minutes = countdown_obj.duration_minutes
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=duration_minutes)
        return render(request, 'countdown_app/countdown.html', {'end_time': end_time})
    else:
        return render(request, 'countdown_app/countdown.html')

def get_remaining_time(request):
    countdown_obj = Countdown.objects.first()
    if countdown_obj:
        duration_minutes = countdown_obj.duration_minutes
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=duration_minutes)
        remaining_time = max(end_time - datetime.datetime.now(), datetime.timedelta())
        return JsonResponse({'remaining_time': str(remaining_time)})
    else:
        return JsonResponse({'remaining_time': '0:00:00'})


