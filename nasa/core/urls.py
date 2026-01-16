from django.urls import path
from .views import lock

urlpatterns = [
    path('', lock, name='lockscreen'),
]