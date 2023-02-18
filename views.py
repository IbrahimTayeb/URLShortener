# views.py
from django.shortcuts import render, redirect
from .models import ShortenedURL

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        shortened_url = ShortenedURL(long_url=long_url)
        shortened_url.save()
        return render(request, 'shortener/result.html', {'shortened_url': shortened_url})
    return render(request, 'shortener/index.html')

def access_url(request, short_url):
    shortened_url = ShortenedURL.objects.get(short_url=short_url)
    return redirect(shortened_url.long_url)
