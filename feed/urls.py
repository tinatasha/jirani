from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.shortcuts import redirect

urlpatterns = [
    url(r'login/feed/', views.feed, name='feed'),
    url(r'signup/', views.signup, name='signup'),
    url(r'login/profile/', views.profile, name="profile"),
    url(r'login/edit_profile/', views.edit_profile, name="edit_profile"),
]
