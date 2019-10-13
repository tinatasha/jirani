from django.shortcuts import render
from .models import Image, Profile
# Create your views here.
def feed(request):
    return render(request, "feed.html")