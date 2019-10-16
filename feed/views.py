from django.shortcuts import render
from .models import Image, UserProfile
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from .forms import *
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

# Create your views here.
def feed(request):
    images = Image.objects.all().filter(time__lte=timezone.now()).order_by('-time')
    return render(request, "feed.html", {"images":images})

def image_details(request):
    images = Image.objects.all().filter(time__lte=timezone.now())
    
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required(login_url="/")
def profile(request):
    current_user = request.user.profile
    user_data = User.objects.get(id=current_user.id)
    user_profile = UserProfile.objects.get(id=current_user.id)
    return render(
        request,
        "registration/profile.html",
        {
            "user_data": user_data,
            "user_profile": user_profile,
            },
        )

@login_required(login_url="login/")  # only logged in users should access this
def edit_profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    
    user_form = UserForm(instance=user)
    
    ProfileInlineFormset = inlineformset_factory(
        User, UserProfile, fields=("photo", "phone", "bio")
        )
    formset = ProfileInlineFormset(instance=user)
    
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(
                    request.POST, request.FILES, instance=created_user
                )
                
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return redirect("profile")
                
        return render(
            request,
            "registration/edit_profile.html",
            {"user_no": user.id, "profile_form": user_form, "formset": formset},
        )
    else:
        raise PermissionDenied
    
    