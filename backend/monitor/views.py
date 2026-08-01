from django.shortcuts import render
import psutil 
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def system_stats(request):
    data = {
        'cpu_percent' : psutil.cpu_percent(interval=1),
        'ram_percent' : psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'uptime_seconds' : psutil.boot_time(), 
    }
    return Response(data)

# Create your views here.
