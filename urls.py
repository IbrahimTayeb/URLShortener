# urls.py
from django.urls import path
from .views import shorten_url, access_url

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_url>/', access_url, name='access_url')
]