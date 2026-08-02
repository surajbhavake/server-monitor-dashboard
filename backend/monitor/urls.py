from django.urls import path
from .views import system_stats

urlpatterns = [
    path('system_stats/',system_stats,name='system_stats')
]
