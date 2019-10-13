from django.shortcuts import render
from .models import Image, Profile
# Create your views here.
def feed(request):
    images = Image.objects.all()
    return render(request, "feed.html", {"images":images})