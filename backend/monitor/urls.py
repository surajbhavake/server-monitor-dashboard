from django.urls import path
from .views import system_stats

urlpatterns = [
    path('system-stats/',system_stats,name='system-stats')
]
