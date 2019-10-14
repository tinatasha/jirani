from django.shortcuts import render
from .models import Image, Profile
from django.utils import timezone
# Create your views here.
def feed(request):
    images = Image.objects.all().filter(time__lte=timezone.now()).order_by('-time')
    return render(request, "feed.html", {"images":images})

def image_details(request):
    images = Image.objects.all().filter(time__lte=timezone.now())
    
def search_results(request):
    images = Image.objects.all().filter()
    return render(request, "search_results.html")